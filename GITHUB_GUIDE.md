# 🚀 GitHub Upload Guide

## Step 1: Create Repo on GitHub
1. Go to github.com → New Repository
2. Name: `Poll-Results-Visualizer`
3. Description: `Survey & poll data analysis with demographics, trends, and Streamlit dashboard`
4. Set to Public
5. DO NOT initialize with README (we have one)
6. Tags: `python`, `data-analysis`, `visualization`, `pandas`, `streamlit`, `survey`

---

## Step 2: Connect Local Project

```bash
cd Poll-Results-Visualizer
git init
git add .
git commit -m "initial commit: full Poll Results Visualizer project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Poll-Results-Visualizer.git
git push -u origin main
```

---

## Step 3: Day-wise Commit Plan (for proof)

| Day | What to commit | Commit message |
|-----|----------------|----------------|
| Day 1 | Folder structure + requirements.txt | `feat: project setup and folder structure` |
| Day 2 | generate_data.py + poll_data.csv | `feat: add synthetic dataset generator` |
| Day 3 | clean_data.py + analyze.py | `feat: data cleaning and analysis module` |
| Day 4 | visualize.py + all charts in outputs/ | `feat: add visualization module and chart outputs` |
| Day 5 | app.py + README + INTERVIEW_PREP.md | `feat: streamlit dashboard and documentation` |

---

## Step 4: Screenshots to take for README

1. `outputs/Q1_bar.png` — bar chart
2. `outputs/Q1_pie.png` — pie chart
3. `outputs/Q1_region_heatmap.png` — heatmap
4. `outputs/Q1_trend.png` — trend chart
5. Streamlit dashboard screenshot (`http://localhost:8501`)
6. GitHub repo page

Add screenshots to `images/` folder and reference in README.

---

## Step 5: Update README images section

```markdown
## 📸 Screenshots

![Bar Chart](images/Q1_bar.png)
![Pie Chart](images/Q1_pie.png)
![Heatmap](images/Q1_region_heatmap.png)
![Dashboard](images/dashboard_screenshot.png)
```
