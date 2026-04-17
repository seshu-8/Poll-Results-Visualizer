"""
analyze.py
Core analysis: vote counts, percentages, demographic breakdowns,
trend over time, and insight generation.
"""

import pandas as pd
import numpy as np


def overall_distribution(df, question_col):
    """
    Returns vote count and percentage for each option of a question.
    """
    counts = df[question_col].value_counts().reset_index()
    counts.columns = ["option", "votes"]
    counts["percentage"] = (counts["votes"] / counts["votes"].sum() * 100).round(2)
    counts = counts.sort_values("votes", ascending=False).reset_index(drop=True)
    return counts


def demographic_breakdown(df, question_col, demographic_col):
    """
    Cross-tab: what % chose each option, grouped by demographic.
    """
    ct = pd.crosstab(df[demographic_col], df[question_col], normalize="index") * 100
    ct = ct.round(2)
    return ct


def leading_option(df, question_col):
    """Return the most voted option for a question."""
    dist = overall_distribution(df, question_col)
    top = dist.iloc[0]
    return top["option"], top["percentage"]


def trend_over_time(df, question_col, top_n=3):
    """
    Monthly trend for the top N options of a question.
    Returns a pivot table: rows=month_name, cols=option, values=count.
    """
    if "month" not in df.columns:
        return None

    top_options = df[question_col].value_counts().head(top_n).index.tolist()
    filtered = df[df[question_col].isin(top_options)]

    trend = filtered.groupby(["month", "month_name", question_col]).size().reset_index(name="count")
    pivot = trend.pivot_table(index=["month", "month_name"], columns=question_col, values="count", fill_value=0)
    pivot = pivot.sort_values("month")
    pivot.index = pivot.index.get_level_values("month_name")
    return pivot


def region_analysis(df, question_col):
    """Region-wise breakdown."""
    return demographic_breakdown(df, question_col, "region")


def generate_insights(df, questions):
    """
    Auto-generate text insights for each question.
    """
    insights = []
    q_cols = [col for col in df.columns if col.startswith("Q") and not col.endswith("_text")]

    for qcol in q_cols:
        q_text = questions.get(qcol, {}).get("text", qcol) if isinstance(questions, dict) else qcol
        dist = overall_distribution(df, qcol)
        leader, pct = dist.iloc[0]["option"], dist.iloc[0]["percentage"]
        last, lpct = dist.iloc[-1]["option"], dist.iloc[-1]["percentage"]

        insight = (
            f"[{qcol}] {q_text}\n"
            f"  → Leading option : '{leader}' with {pct}% of votes\n"
            f"  → Least preferred: '{last}' with {lpct}% of votes\n"
            f"  → Total responses: {dist['votes'].sum()}\n"
        )
        insights.append(insight)

    return "\n".join(insights)


def summary_table(df, questions):
    """
    Returns a summary DataFrame: question | leading option | % votes | total responses
    """
    rows = []
    q_cols = [col for col in df.columns if col.startswith("Q") and not col.endswith("_text")]

    for qcol in q_cols:
        q_text = questions.get(qcol, {}).get("text", qcol) if isinstance(questions, dict) else qcol
        dist = overall_distribution(df, qcol)
        rows.append({
            "Question ID": qcol,
            "Question": q_text,
            "Leading Option": dist.iloc[0]["option"],
            "Leading %": dist.iloc[0]["percentage"],
            "Runner-up": dist.iloc[1]["option"] if len(dist) > 1 else "N/A",
            "Runner-up %": dist.iloc[1]["percentage"] if len(dist) > 1 else 0,
            "Total Responses": dist["votes"].sum()
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    from clean_data import load_data, clean_data
    from generate_data import generate_poll_data

    # Generate + clean
    df_raw, questions = generate_poll_data(500)
    df_raw.to_csv("data/poll_data.csv", index=False)
    df = clean_data(load_data())

    # Test
    print(overall_distribution(df, "Q1"))
    print(demographic_breakdown(df, "Q1", "region"))
    print(generate_insights(df, questions))
    print(summary_table(df, questions))
