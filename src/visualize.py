"""
visualize.py
All chart generation: bar, pie, stacked bar, trend line, heatmap.
All charts saved to outputs/ folder.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

# Output directory
OUTDIR = "outputs"
os.makedirs(OUTDIR, exist_ok=True)

# Theme
PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2",
           "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"]
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "#F8F9FA",
    "axes.grid": True,
    "grid.color": "#DDDDDD",
    "grid.linestyle": "--",
    "font.family": "DejaVu Sans",
})


def bar_chart(dist_df, title, xlabel, ylabel="Votes", filename="bar_chart.png"):
    """Horizontal bar chart for option distribution."""
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = PALETTE[:len(dist_df)]

    bars = ax.barh(dist_df["option"], dist_df["votes"], color=colors, edgecolor="white", height=0.6)

    # Labels on bars
    for bar, pct in zip(bars, dist_df["percentage"]):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
                f"{pct}%", va="center", fontsize=10, fontweight="bold")

    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel(ylabel, fontsize=11)
    ax.set_ylabel(xlabel, fontsize=11)
    ax.invert_yaxis()
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")
    return path


def pie_chart(dist_df, title, filename="pie_chart.png"):
    """Pie chart for option distribution."""
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        dist_df["votes"],
        labels=dist_df["option"],
        autopct="%1.1f%%",
        startangle=140,
        colors=PALETTE[:len(dist_df)],
        pctdistance=0.82,
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    for t in autotexts:
        t.set_fontsize(9)
        t.set_fontweight("bold")

    ax.set_title(title, fontsize=14, fontweight="bold", pad=16)
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")
    return path


def stacked_bar_chart(crosstab_df, title, filename="stacked_bar.png"):
    """100% stacked bar chart for demographic breakdown."""
    fig, ax = plt.subplots(figsize=(12, 6))
    crosstab_df.plot(
        kind="bar", stacked=True, ax=ax,
        color=PALETTE[:len(crosstab_df.columns)],
        edgecolor="white", width=0.65
    )
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Group", fontsize=11)
    ax.set_ylabel("Percentage (%)", fontsize=11)
    ax.legend(title="Options", bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=9)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")
    return path


def trend_line_chart(trend_pivot, title, filename="trend_chart.png"):
    """Line chart: option popularity over months."""
    if trend_pivot is None:
        print("No date data available for trend chart.")
        return None

    fig, ax = plt.subplots(figsize=(12, 5))
    for i, col in enumerate(trend_pivot.columns):
        ax.plot(trend_pivot.index, trend_pivot[col], marker="o",
                label=col, linewidth=2.5, color=PALETTE[i], markersize=6)

    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Responses", fontsize=11)
    ax.legend(fontsize=10)
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")
    return path


def heatmap_chart(crosstab_df, title, filename="heatmap.png"):
    """Heatmap for region vs option percentages."""
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(crosstab_df, annot=True, fmt=".1f", cmap="YlOrRd",
                linewidths=0.5, ax=ax, cbar_kws={"label": "%"})
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")
    return path


def summary_dashboard(summary_df, filename="summary_dashboard.png"):
    """Summary table rendered as an image."""
    fig, ax = plt.subplots(figsize=(14, 3 + len(summary_df) * 0.5))
    ax.axis("off")

    col_widths = [0.06, 0.30, 0.18, 0.10, 0.18, 0.10, 0.08]
    table = ax.table(
        cellText=summary_df.values,
        colLabels=summary_df.columns,
        cellLoc="center",
        loc="center",
        colWidths=col_widths
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.8)

    # Style header
    for j in range(len(summary_df.columns)):
        table[0, j].set_facecolor("#4C72B0")
        table[0, j].set_text_props(color="white", fontweight="bold")

    # Alternate row colors
    for i in range(1, len(summary_df) + 1):
        for j in range(len(summary_df.columns)):
            table[i, j].set_facecolor("#EEF2FF" if i % 2 == 0 else "white")

    plt.title("Poll Summary - All Questions", fontsize=14, fontweight="bold", pad=16)
    plt.tight_layout()
    path = os.path.join(OUTDIR, filename)
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")
    return path


if __name__ == "__main__":
    print("visualize.py loaded successfully. Run main.py to generate all charts.")
