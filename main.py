"""
main.py
Poll Results Visualizer - Main Entry Point
Run: python main.py
"""

import os
import sys
sys.path.insert(0, "src")

from generate_data import generate_poll_data
from clean_data import load_data, clean_data, inspect_data
from analyze import (
    overall_distribution, demographic_breakdown,
    trend_over_time, region_analysis,
    generate_insights, summary_table
)
from visualize import (
    bar_chart, pie_chart, stacked_bar_chart,
    trend_line_chart, heatmap_chart, summary_dashboard
)

os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


def main():
    print("=" * 60)
    print("  POLL RESULTS VISUALIZER")
    print("=" * 60)

    # ──────────────────────────────────────────────
    # STEP 1: Generate synthetic poll data
    # ──────────────────────────────────────────────
    print("\n[1/6] Generating synthetic poll dataset...")
    df_raw, questions = generate_poll_data(n=500)
    df_raw.to_csv("data/poll_data.csv", index=False)
    print(f"  Dataset saved: data/poll_data.csv  ({len(df_raw)} rows)")

    # ──────────────────────────────────────────────
    # STEP 2: Load & Clean
    # ──────────────────────────────────────────────
    print("\n[2/6] Loading and cleaning data...")
    df = load_data("data/poll_data.csv")
    inspect_data(df)
    df = clean_data(df)
    df.to_csv("data/poll_data_clean.csv", index=False)
    print("  Clean data saved: data/poll_data_clean.csv")

    # ──────────────────────────────────────────────
    # STEP 3: Analysis
    # ──────────────────────────────────────────────
    print("\n[3/6] Running analysis...")
    q_cols = [col for col in df.columns if col.startswith("Q") and not col.endswith("_text")]

    for qcol in q_cols:
        dist = overall_distribution(df, qcol)
        print(f"\n  {qcol} - {questions[qcol]['text']}")
        print(dist.to_string(index=False))

    summary = summary_table(df, questions)
    summary.to_csv("outputs/summary_table.csv", index=False)
    print("\n  Summary table saved: outputs/summary_table.csv")

    # ──────────────────────────────────────────────
    # STEP 4: Visualizations
    # ──────────────────────────────────────────────
    print("\n[4/6] Generating charts...")

    for qcol in q_cols:
        q_text = questions[qcol]["text"]
        dist = overall_distribution(df, qcol)

        # Bar chart
        bar_chart(
            dist,
            title=f"Q: {q_text}",
            xlabel="Options",
            filename=f"{qcol}_bar.png"
        )

        # Pie chart
        pie_chart(
            dist,
            title=f"Q: {q_text}",
            filename=f"{qcol}_pie.png"
        )

        # Region breakdown - stacked bar
        region_ct = region_analysis(df, qcol)
        stacked_bar_chart(
            region_ct,
            title=f"Region-wise: {q_text}",
            filename=f"{qcol}_region_stacked.png"
        )

        # Region heatmap
        heatmap_chart(
            region_ct,
            title=f"Region Heatmap: {q_text}",
            filename=f"{qcol}_region_heatmap.png"
        )

        # Age group breakdown
        age_ct = demographic_breakdown(df, qcol, "age_group")
        stacked_bar_chart(
            age_ct,
            title=f"Age Group Breakdown: {q_text}",
            filename=f"{qcol}_age_stacked.png"
        )

        # Trend over time
        trend = trend_over_time(df, qcol, top_n=3)
        trend_line_chart(
            trend,
            title=f"Monthly Trend (Top 3): {q_text}",
            filename=f"{qcol}_trend.png"
        )

    # Summary dashboard image
    summary_dashboard(summary, filename="summary_dashboard.png")

    # ──────────────────────────────────────────────
    # STEP 5: Text Insights
    # ──────────────────────────────────────────────
    print("\n[5/6] Generating text insights...")
    insights = generate_insights(df, questions)
    print(insights)
    with open("outputs/insights.txt", "w", encoding="utf-8") as f:
        f.write(insights)
    print("  Insights saved: outputs/insights.txt")

    # ──────────────────────────────────────────────
    # STEP 6: Summary
    # ──────────────────────────────────────────────
    print("\n[6/6] Done!")
    print("=" * 60)
    print("  OUTPUT FILES:")
    for fname in sorted(os.listdir("outputs")):
        print(f"    outputs/{fname}")
    print("=" * 60)


if __name__ == "__main__":
    main()
