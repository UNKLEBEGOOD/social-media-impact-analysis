import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Social Media Impact Dashboard", layout="wide")
sns.set_style('whitegrid')

# ---------- Load data ----------
@st.cache_data
def load_data():
    return pd.read_csv('data/clean/social_media_impact_clean.csv')

df = load_data()

# ---------- Sidebar filters ----------
st.sidebar.header("Filters")

academic_levels = st.sidebar.multiselect(
    "Academic Level",
    options=sorted(df['Academic_Level'].unique()),
    default=sorted(df['Academic_Level'].unique())
)

genders = st.sidebar.multiselect(
    "Gender",
    options=sorted(df['Gender'].unique()),
    default=sorted(df['Gender'].unique())
)

platforms = st.sidebar.multiselect(
    "Primary Platform",
    options=sorted(df['Primary_Platform'].unique()),
    default=sorted(df['Primary_Platform'].unique())
)

filtered = df[
    df['Academic_Level'].isin(academic_levels) &
    df['Gender'].isin(genders) &
    df['Primary_Platform'].isin(platforms)
]

st.sidebar.markdown("---")
st.sidebar.caption(f"Showing {len(filtered):,} of {len(df):,} students")

# ---------- Title ----------
st.title("Social Media Impact on Student Life")
st.caption("Data-driven insights for parents, teachers, and students")

if len(filtered) == 0:
    st.warning("No students match the current filters. Adjust the filters in the sidebar.")
    st.stop()

# ---------- KPI row ----------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Students", f"{len(filtered):,}")
col2.metric("Avg Daily Usage", f"{filtered['Daily_Usage_Hours'].mean():.1f} hrs")
col3.metric("Avg Sleep", f"{filtered['Sleep_Duration_Hours'].mean():.1f} hrs")
col4.metric("Avg GPA", f"{filtered['Academic_Performance_GPA'].mean():.2f}")

st.markdown("---")

# ---------- Overall Impact summary ----------
st.subheader("Self-Reported Overall Impact")

impact_order = ['Beneficial', 'Neutral', 'Negative']
impact_colors = {'Beneficial': '#2ca25f', 'Neutral': '#fec44f', 'Negative': '#de2d26'}

c1, c2 = st.columns([1, 2])

with c1:
    counts = filtered['Overall_Impact'].value_counts()
    for label in impact_order:
        if label in counts.index:
            pct = counts[label] / len(filtered) * 100
            avg_hrs = filtered.loc[filtered['Overall_Impact'] == label, 'Daily_Usage_Hours'].mean()
            st.markdown(f"**{label}** — {counts[label]:,} students ({pct:.0f}%), {avg_hrs:.1f} hrs/day avg")

with c2:
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.boxplot(data=filtered, x='Overall_Impact', y='Daily_Usage_Hours',
                order=[l for l in impact_order if l in filtered['Overall_Impact'].unique()],
                hue='Overall_Impact', palette=impact_colors, legend=False, ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("Daily Usage (Hours)")
    st.pyplot(fig)

st.info("Students who report social media as harming them consistently use it far more "
        "than those who report it as beneficial — this is the clearest pattern in the data.")

st.markdown("---")

# ---------- Relationship charts ----------
st.subheader("How Usage Relates to Wellbeing and Performance")

tab1, tab2, tab3, tab4 = st.tabs(["Sleep", "Academic Performance", "Stress", "Mental Health"])

def scatter_tab(container, y_col, y_label, color, insight_text):
    with container:
        corr = filtered['Daily_Usage_Hours'].corr(filtered[y_col])
        fig, ax = plt.subplots(figsize=(8, 4.5))
        sns.scatterplot(data=filtered, x='Daily_Usage_Hours', y=y_col, alpha=0.4, color=color, ax=ax)
        ax.set_xlabel("Daily Usage (Hours)")
        ax.set_ylabel(y_label)
        st.pyplot(fig)
        st.metric("Correlation with Daily Usage", f"{corr:.2f}")
        st.caption(insight_text)

scatter_tab(tab1, 'Sleep_Duration_Hours', 'Sleep Duration (Hours)', '#2c7fb8',
    "Higher usage is strongly linked to less sleep. Students averaging 2 hrs/day sleep "
    "9-10 hrs; those at 10+ hrs/day often sleep only 4-6 hrs.")

scatter_tab(tab2, 'Academic_Performance_GPA', 'GPA', '#2c7fb8',
    "Higher usage is strongly linked to lower GPA. Students at 2 hrs/day average 3.5-4.0; "
    "those at 10+ hrs/day often drop to 2.5-3.0 or lower.")

scatter_tab(tab3, 'Perceived_Stress_Score', 'Perceived Stress Score', '#de2d26',
    "Higher usage is strongly linked to higher stress. Students at 2 hrs/day average a "
    "stress score near 5-10; those at 10+ hrs/day often average 25-30+.")

scatter_tab(tab4, 'Mental_Health_Index', 'Mental Health Index', '#de2d26',
    "The strongest relationship in the dataset. Students at 2 hrs/day average a mental "
    "health score near 90-100; those at 12-14 hrs/day often drop to 40-60.")

st.markdown("---")

# ---------- Platform comparison ----------
st.subheader("Usage by Primary Platform")
platform_order = filtered.groupby('Primary_Platform')['Daily_Usage_Hours'].mean().sort_values(ascending=False).index

fig, ax = plt.subplots(figsize=(10, 4.5))
sns.boxplot(data=filtered, x='Primary_Platform', y='Daily_Usage_Hours',
            hue='Primary_Platform', order=platform_order, legend=False, palette='Set2', ax=ax)
ax.set_xlabel("Primary Platform")
ax.set_ylabel("Daily Usage (Hours)")
plt.xticks(rotation=20)
st.pyplot(fig)

st.caption("Average usage is nearly identical across all platforms (5.1-5.5 hrs/day) — "
           "the specific app matters far less than total time spent.")

st.markdown("---")
st.caption("Built with Streamlit · Data: 4,500 students · Odoh Ekenedirichukwu Johnpaul")