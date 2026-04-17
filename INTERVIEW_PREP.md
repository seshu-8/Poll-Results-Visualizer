# 🎤 Interview Preparation — Poll Results Visualizer

---

## HR Questions

**Q1: Tell me about this project.**
> "I built a Poll Results Visualizer that takes raw survey data, cleans it, runs demographic and trend analysis, and generates visualizations using Python. The project mimics how companies like SurveyMonkey and YouGov process poll data to make decisions. It includes a Streamlit dashboard for interactive exploration."

**Q2: Why did you build this?**
> "I wanted a project that combines data cleaning, EDA, and visualization — all core skills for a data/business analyst role. Poll data is universal across industries, so it's highly relatable in interviews."

**Q3: What was the hardest part?**
> "Designing the demographic breakdown cleanly using pd.crosstab() with normalization, and making the stacked bar chart readable with proper percentage formatting."

---

## Technical Questions

**Q4: How did you handle missing data?**
> "I used `df.dropna(subset=[critical_cols])` for rows missing key fields like respondent_id or region. For strings, I applied `.str.strip()` to catch whitespace-as-null issues."

**Q5: How do you calculate percentage distribution?**
> "Using `value_counts()` divided by total count, multiplied by 100 and rounded to 2 decimals. I encapsulated this in an `overall_distribution()` function for reuse."

**Q6: What is `pd.crosstab()` and why did you use it?**
> "It creates a frequency table of two categorical variables. With `normalize='index'`, each row sums to 1.0, so multiplying by 100 gives row-wise percentages — perfect for demographic breakdowns."

**Q7: What is EDA?**
> "Exploratory Data Analysis — the process of summarizing, visualizing, and understanding a dataset before modeling. It includes checking distributions, nulls, outliers, and relationships between variables."

**Q8: Why Matplotlib over Plotly?**
> "Matplotlib gives pixel-perfect static charts for reports and GitHub screenshots. I also support Plotly for interactive use — both are included in this project."

**Q9: How would you scale this for 1 million responses?**
> "Use chunked CSV reading with `pd.read_csv(chunksize=...)`, or migrate to Spark/Dask for distributed processing. The modular function design makes swapping the data layer easy."

**Q10: What's next for this project?**
> "Live Google Forms integration via API, NLP sentiment on open-ended questions, and a Power BI export option."

---

## Quick Talking Points for Resume

- "Processed and analyzed 500+ poll responses using Python and Pandas"
- "Generated 6+ chart types (bar, pie, stacked bar, heatmap, trend) using Matplotlib and Seaborn"
- "Built demographic breakdowns by region, age group, gender, and education"
- "Deployed an interactive dashboard using Streamlit"
- "Automated text insight generation for stakeholder reporting"
