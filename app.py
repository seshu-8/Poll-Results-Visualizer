"""
app.py
Streamlit Dashboard for Poll Results Visualizer
Run: streamlit run app.py
"""

import sys
sys.path.insert(0, "src")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from generate_data import generate_poll_data
from clean_data import clean_data
from analyze import (
    overall_distribution, demographic_breakdown,
    trend_over_time, region_analysis, summary_table
)
from visualize import (
    bar_chart, pie_chart, stacked_bar_chart,
    trend_line_chart, heatmap_chart
)

# ── Page Config ──────────────────────────────────
st.set_page_config(
    page_title="Poll Results Visualizer",
    page_icon="📊",
    layout="wide"
)

# ── Load Data ────────────────────────────────────
@st.cache_data
def load():
    if not os.path.exists("data/poll_data_clean.csv"):
        df_raw, questions = generate_poll_data(500)
        os.makedirs("data", exist_ok=True)
        df_raw.to_csv("data/poll_data.csv", index=False)
        df = clean_data(df_raw)
        df.to_csv("data/poll_data_clean.csv", index=False)
    else:
        df = pd.read_csv("data/poll_data_clean.csv", parse_dates=["date"])
        df["month"] = df["date"].dt.month
        df["month_name"] = df["date"].dt.strftime("%b")
        _, questions = generate_poll_data(500)
    return df, questions

df, questions = load()
q_cols = [col for col in df.columns if col.startswith("Q") and not col.endswith("_text")]

# ── Sidebar ──────────────────────────────────────
st.sidebar.title("🔧 Controls")
selected_q = st.sidebar.selectbox(
    "Select Question",
    options=q_cols,
    format_func=lambda x: f"{x}: {questions[x]['text'][:40]}..."
)
chart_type = st.sidebar.radio("Chart Type", ["Bar", "Pie", "Both"])
demo_col = st.sidebar.selectbox(
    "Demographic Breakdown",
    ["region", "age_group", "gender", "education"]
)
show_trend = st.sidebar.checkbox("Show Monthly Trend", value=True)
show_heatmap = st.sidebar.checkbox("Show Region Heatmap", value=True)

# ── Header ───────────────────────────────────────
st.title("📊 Poll Results Visualizer")
st.markdown("**Analyze and visualize survey/poll data with demographic breakdowns and trends.**")
st.divider()

# ── KPI Metrics ──────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
dist = overall_distribution(df, selected_q)
leader = dist.iloc[0]
col1.metric("Total Responses", f"{len(df):,}")
col2.metric("Leading Option", leader["option"])
col3.metric("Leading Share", f"{leader['percentage']}%")
col4.metric("Options Count", len(dist))

st.divider()

# ── Distribution Charts ───────────────────────────
st.subheader(f"📌 {questions[selected_q]['text']}")

os.makedirs("outputs", exist_ok=True)
if chart_type in ["Bar", "Both"]:
    bar_path = bar_chart(dist, title=questions[selected_q]['text'],
                         xlabel="Options", filename=f"dash_{selected_q}_bar.png")
    st.image(bar_path, caption="Vote Distribution - Bar Chart", use_column_width=True)

if chart_type in ["Pie", "Both"]:
    pie_path = pie_chart(dist, title=questions[selected_q]['text'],
                         filename=f"dash_{selected_q}_pie.png")
    st.image(pie_path, caption="Vote Distribution - Pie Chart", use_column_width=True)

# ── Raw Distribution Table ────────────────────────
with st.expander("📋 View Distribution Table"):
    st.dataframe(dist, use_container_width=True)

st.divider()

# ── Demographic Breakdown ─────────────────────────
st.subheader(f"👥 Breakdown by {demo_col.replace('_', ' ').title()}")
demo_ct = demographic_breakdown(df, selected_q, demo_col)
stacked_path = stacked_bar_chart(
    demo_ct,
    title=f"{demo_col.title()} Breakdown: {questions[selected_q]['text'][:50]}",
    filename=f"dash_{selected_q}_{demo_col}_stacked.png"
)
st.image(stacked_path, use_column_width=True)

with st.expander("📋 View Crosstab Data"):
    st.dataframe(demo_ct, use_container_width=True)

# ── Trend Chart ───────────────────────────────────
if show_trend:
    st.divider()
    st.subheader("📈 Monthly Trend (Top 3 Options)")
    trend = trend_over_time(df, selected_q, top_n=3)
    if trend is not None:
        trend_path = trend_line_chart(
            trend,
            title=f"Monthly Trend: {questions[selected_q]['text'][:50]}",
            filename=f"dash_{selected_q}_trend.png"
        )
        st.image(trend_path, use_column_width=True)

# ── Heatmap ───────────────────────────────────────
if show_heatmap:
    st.divider()
    st.subheader("🗺️ Region-wise Heatmap")
    region_ct = region_analysis(df, selected_q)
    heatmap_path = heatmap_chart(
        region_ct,
        title=f"Region Heatmap: {questions[selected_q]['text'][:50]}",
        filename=f"dash_{selected_q}_heatmap.png"
    )
    st.image(heatmap_path, use_column_width=True)

# ── Summary Table ─────────────────────────────────
st.divider()
st.subheader("📊 All Questions Summary")
summary = summary_table(df, questions)
st.dataframe(summary, use_container_width=True)

# ── Raw Data Preview ──────────────────────────────
st.divider()
with st.expander("🗃️ Raw Dataset Preview (first 100 rows)"):
    st.dataframe(df.head(100), use_container_width=True)

st.caption("Poll Results Visualizer | Built for placements & internships | GitHub-ready project")
