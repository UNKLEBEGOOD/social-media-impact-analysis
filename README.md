
# Social Media Impact on Student Life

A data analysis project exploring how daily social media usage relates to student sleep, academic performance, stress, and mental wellbeing — built to support informed, constructive conversations between parents, teachers, and students about healthy social media habits.

## Project Brief

As a data analyst consulting for the Ministry of Information and Communication Technology, the task was to explore a dataset of student social media usage and present clear, non-technical findings at a Parent-Teacher-Student Conference.

## Dataset

4,500 student records covering:
- **Demographics:** Age, Gender, Academic Level
- **Usage patterns:** Daily usage hours, weekend usage, primary platform, device type, late-night usage
- **Outcomes:** Sleep duration/quality, perceived stress, mental health index, GPA, self-reported overall impact

## Repository Structure

```
├── data/
│   ├── raw/                          # Original dataset
│   └── clean/                        # Cleaned dataset (missing values handled)
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # Profiling, missing values, outlier checks
│   ├── 02_eda.ipynb                  # Exploratory analysis, correlations, insights
│   └── 03_visuals.ipynb              # Presentation-ready chart exports
├── reports/
│   └── Social_Media_Impact_Analysis_Report.pdf
├── visuals/                           # Exported chart PNGs
└── README.md
```

## Methodology

- Checked the dataset for completeness and consistency: two columns (`Perceived_Stress_Score`, `Academic_Performance_GPA`) had missing values, filled using the **median within each student's academic level group** rather than a single overall average, to preserve real differences between High School, Undergraduate, and Postgraduate students.
- Confirmed no duplicate records.
- Ran an IQR-based outlier check across all numeric variables; all flagged values fell within realistic human ranges, so they were retained as genuine variation rather than removed.
- Measured relationships using Pearson correlation and visualized patterns for a non-technical audience.

## Key Findings

Demographic factors (age, gender, academic level) and platform choice showed **little to no effect** on usage — averages stayed within minutes of each other across every group. What mattered was **total daily usage hours**, which showed strong, consistent relationships with every outcome tracked:

| Relationship | Correlation |
|---|---|
| Usage → Mental Health Index | **−0.85** (strongest) |
| Usage → Perceived Stress | **+0.75** |
| Usage → Sleep Duration | **−0.72** |
| Usage → Academic Performance (GPA) | **−0.70** |

Students who self-report social media as **Negative** for them use it nearly **3x more** on average (12.3 hrs/day) than students who report it as **Beneficial** (4.4 hrs/day) — and 82% of students fall into the Beneficial group.

## Key Insights & Recommendations

1. **Heavy usage (10+ hrs/day) is where negative outcomes concentrate** — encourage keeping daily usage below ~8 hours rather than discouraging use entirely.
2. **Higher usage is strongly linked to reduced sleep** — total usage volume matters more than late-night timing alone.
3. **Higher usage is strongly linked to lower GPA** — protected, phone-free study periods are likely more effective than a blanket time limit.
4. **Higher usage is linked to more stress and poorer mental health** — conversations should address *how* students use social media (e.g. social comparison), not just how long.

Full detail, evidence, and charts for each insight are in the [Analysis Report](reports/Social_Media_Impact_Analysis_Report.pdf).

## Tools Used

Python (pandas, matplotlib, seaborn) in Jupyter Notebook · Power BI (interactive dashboard)

## Author

Odoh Ekenedirichukwu Johnpaul — [LinkedIn](https://linkedin.com/in/kene08)
