"""
clean_data.py
Handles loading, validating, and cleaning the poll dataset.
"""

import pandas as pd
import numpy as np


def load_data(filepath="data/poll_data.csv"):
    """Load CSV into a DataFrame."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns.")
    return df


def inspect_data(df):
    """Print basic inspection report."""
    print("\n--- DATA INSPECTION ---")
    print(f"Shape      : {df.shape}")
    print(f"Columns    : {list(df.columns)}")
    print(f"\nNull Values:\n{df.isnull().sum()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nSample:\n{df.head(3)}")


def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Handle nulls
    - Standardize date column
    - Strip whitespace from string columns
    """
    original_len = len(df)

    # Remove duplicate respondent IDs
    df = df.drop_duplicates(subset=["respondent_id"])
    print(f"Removed {original_len - len(df)} duplicate rows.")

    # Strip whitespace
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip()

    # Parse date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["month"] = df["date"].dt.month
        df["month_name"] = df["date"].dt.strftime("%b")
        df["week"] = df["date"].dt.isocalendar().week.astype(int)

    # Drop rows with critical nulls
    critical_cols = ["respondent_id", "region", "age_group"]
    before = len(df)
    df = df.dropna(subset=critical_cols)
    print(f"Dropped {before - len(df)} rows with critical nulls.")

    print(f"Final clean dataset: {len(df)} rows.")
    return df


def get_question_columns(df):
    """Return list of question column IDs (Q1, Q2, ...)."""
    return [col for col in df.columns if col.startswith("Q") and not col.endswith("_text")]


if __name__ == "__main__":
    df = load_data()
    inspect_data(df)
    df_clean = clean_data(df)
    df_clean.to_csv("data/poll_data_clean.csv", index=False)
    print("Clean data saved.")
