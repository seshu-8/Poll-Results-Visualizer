"""
generate_data.py
Generates a synthetic poll dataset for the Poll Results Visualizer.
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_poll_data(n=500, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    # Config
    questions = {
        "Q1": {
            "text": "Which programming language do you prefer?",
            "options": ["Python", "Java", "C++", "JavaScript", "Go"],
            "weights": [0.40, 0.20, 0.15, 0.18, 0.07]
        },
        "Q2": {
            "text": "How satisfied are you with online learning?",
            "options": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"],
            "weights": [0.25, 0.35, 0.20, 0.12, 0.08]
        },
        "Q3": {
            "text": "What is your preferred work mode?",
            "options": ["Remote", "Hybrid", "On-site"],
            "weights": [0.45, 0.35, 0.20]
        },
        "Q4": {
            "text": "Which cloud platform do you use most?",
            "options": ["AWS", "Azure", "GCP", "IBM Cloud", "None"],
            "weights": [0.38, 0.28, 0.18, 0.06, 0.10]
        }
    }

    regions = ["North", "South", "East", "West", "Central"]
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
    genders = ["Male", "Female", "Non-binary", "Prefer not to say"]
    education = ["High School", "Bachelor's", "Master's", "PhD", "Other"]

    start_date = datetime(2024, 1, 1)

    records = []
    for i in range(n):
        region = random.choices(regions, weights=[0.25, 0.20, 0.20, 0.20, 0.15])[0]
        age = random.choices(age_groups, weights=[0.30, 0.35, 0.18, 0.10, 0.07])[0]
        gender = random.choices(genders, weights=[0.48, 0.46, 0.04, 0.02])[0]
        edu = random.choices(education, weights=[0.10, 0.45, 0.30, 0.10, 0.05])[0]
        date = start_date + timedelta(days=random.randint(0, 179))

        row = {
            "respondent_id": f"R{i+1:04d}",
            "date": date.strftime("%Y-%m-%d"),
            "region": region,
            "age_group": age,
            "gender": gender,
            "education": edu,
        }

        for qid, qdata in questions.items():
            row[qid] = random.choices(qdata["options"], weights=qdata["weights"])[0]
            row[f"{qid}_text"] = qdata["text"]

        records.append(row)

    df = pd.DataFrame(records)
    return df, questions


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df, _ = generate_poll_data(500)
    df.to_csv("data/poll_data.csv", index=False)
    print(f"Dataset created: {len(df)} rows")
    print(df.head())
