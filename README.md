# 📊 Poll Results Visualizer

> A complete data analysis and visualization project for survey/poll data — built for **Data Analyst**, **Business Analyst**, and **Research Analyst** roles.

---

## 🧩 Problem Statement

Organizations collect thousands of survey responses but lack quick tools to:
- Identify leading opinions across questions
- Break down results by region, age, or gender
- Track trends over time
- Generate automated insights

This project solves that with a full pipeline from raw poll data → clean analysis → visual insights.

---

## ✅ Features

| Feature | Description |
|---|---|
| 🎲 Synthetic Data Generator | Creates realistic 500-row poll datasets |
| 🧹 Data Cleaning | Deduplication, null handling, date parsing |
| 📊 Distribution Charts | Bar + Pie charts per question |
| 👥 Demographic Breakdown | Region, Age, Gender, Education (stacked bar) |
| 🗺️ Region Heatmap | Seaborn heatmap for geographic patterns |
| 📈 Monthly Trend | Line chart tracking option popularity over time |
| 💡 Auto Insights | Text summaries with leading options & stats |
| 📋 Summary Table | One table across all questions |
| 🖥️ Streamlit Dashboard | Interactive web UI for exploring all charts |

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib + Seaborn** — static charts
- **Plotly** — interactive charts
- **Streamlit** — web dashboard

---

## 📁 Folder Structure

```
Poll-Results-Visualizer/
│
├── data/                    # Raw and cleaned CSV files
├── notebooks/               # Jupyter notebooks for EDA
├── src/
│   ├── generate_data.py     # Synthetic dataset generator
│   ├── clean_data.py        # Data cleaning functions
│   ├── analyze.py           # Analysis: distribution, trends, insights
│   └── visualize.py         # All chart generation functions
├── outputs/                 # Generated charts + insights
├── images/                  # Screenshots for README
├── main.py                  # Run everything end-to-end
├── app.py                   # Streamlit interactive dashboard
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/Poll-Results-Visualizer.git
cd Poll-Results-Visualizer

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Option 1: Full pipeline (CLI)
```bash
python main.py
```
Generates data → cleans → analyzes → saves all charts to `outputs/`

### Option 2: Interactive Dashboard
```bash
streamlit run app.py
```
Opens a web app at `http://localhost:8501`

---

## 📤 Sample Outputs

- `outputs/Q1_bar.png` — Bar chart: Programming language preference
- `outputs/Q1_pie.png` — Pie chart
- `outputs/Q1_region_heatmap.png` — Region heatmap
- `outputs/Q1_trend.png` — Monthly trend
- `outputs/summary_table.csv` — Aggregated summary
- `outputs/insights.txt` — Auto-generated text insights

---

## 💡 Key Insights (Sample)

```
[Q1] Which programming language do you prefer?
  → Leading option : 'Python' with 40.2% of votes
  → Least preferred: 'Go' with 6.8% of votes

[Q3] What is your preferred work mode?
  → Leading option : 'Remote' with 45.1% of votes
  → Least preferred: 'On-site' with 19.9% of votes
```

---

## 🔮 Future Improvements

- [ ] Live Google Forms integration via API
- [ ] NLP sentiment analysis on open-ended responses
- [ ] Power BI / Tableau export
- [ ] Real-time polling with database backend
- [ ] PDF report auto-generation

---

## 🎓 Interview Talking Points

1. **"How did you handle missing data?"** → `dropna()` on critical columns, whitespace stripping, date parsing
2. **"What does your pipeline look like?"** → Data ingestion → Cleaning → Aggregation → Visualization → Insights
3. **"How do you calculate percentages?"** → `value_counts() / total * 100`
4. **"What is a crosstab?"** → `pd.crosstab()` normalizing by row to get % per group
5. **"How do you make it scalable?"** → Parameterized functions, modular `src/` design, CSV input-agnostic

---

## 👤 Author

**Seshu** | Student | Andhra Pradesh, India
GitHub: https://github.com/seshu-8/Poll-Results-Visualizer/tree/main

---

## 📄 License

MIT License — free to use, modify, and share.
