import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Make sure the CSV is in the same folder as this script
df = pd.read_csv('global_cancer_patients_2015_2024.csv')

# Set page config
st.set_page_config(page_title="Cancer Data Dashboard", layout="wide")
st.title("🌍 Global Cancer Data Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_country = st.sidebar.multiselect(
    "Select Country/Region", 
    options=df['Country_Region'].unique(), 
    default=df['Country_Region'].unique()
)
filtered_df = df[df['Country_Region'].isin(selected_country)]

# Overview Stats
st.subheader("📊 Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Patients", f"{len(filtered_df):,}")
col2.metric("Avg. Treatment Cost (USD)", f"${filtered_df['Treatment_Cost_USD'].mean():,.2f}")
col3.metric("Avg. Severity Score", f"{filtered_df['Target_Severity_Score'].mean():.2f}")

# 1. Trend of Patients Over Time
yearly_trend = filtered_df.groupby('Year').size()
fig1, ax1 = plt.subplots()
yearly_trend.plot(marker='o', ax=ax1)
ax1.set_title('Trend of Global Cancer Patients (2015–2024)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Patients')
ax1.grid(True)
st.pyplot(fig1)

# 2. Top 5 Cancer Types by Avg Treatment Cost
avg_cost_by_cancer = (
    filtered_df
    .groupby('Cancer_Type')['Treatment_Cost_USD']
    .mean()
    .sort_values(ascending=False)
    .head(5)
)
fig2, ax2 = plt.subplots()
avg_cost_by_cancer.plot(kind='bar', color='salmon', ax=ax2)
ax2.set_title('Top 5 Cancer Types by Average Treatment Cost')
ax2.set_ylabel('Avg Treatment Cost (USD)')
ax2.set_xticklabels(avg_cost_by_cancer.index, rotation=45)
st.pyplot(fig2)

# 3. Severity vs Cost Scatter
fig3, ax3 = plt.subplots()
sns.scatterplot(
    data=filtered_df, 
    x='Target_Severity_Score', 
    y='Treatment_Cost_USD', 
    hue='Cancer_Stage', 
    ax=ax3
)
ax3.set_title('Severity Score vs Treatment Cost by Cancer Stage')
ax3.set_xlabel('Severity Score')
ax3.set_ylabel('Treatment Cost (USD)')
st.pyplot(fig3)

# 4. Correlation Heatmap
numerical_df = filtered_df.select_dtypes(include='number')
corr = numerical_df.corr()
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax4)
ax4.set_title('Correlation Matrix')
st.pyplot(fig4)

# 5. Average Survival by Age Group
# Create Age_Group if not present
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81+']
filtered_df['Age_Group'] = pd.cut(filtered_df['Age'], bins=bins, labels=labels, right=False)
avg_survival_by_age = (
    filtered_df
    .groupby('Age_Group', observed=False)['Survival_Years']
    .mean()
)
fig5, ax5 = plt.subplots()
avg_survival_by_age.plot(kind='bar', color='lightgreen', ax=ax5)
ax5.set_title('Average Survival Years by Age Group')
ax5.set_ylabel('Avg Survival Years')
st.pyplot(fig5)

# Footer
st.markdown("---")
st.markdown("Created by **Agwu Collins Obinna** | ✉️ collinsobinna68@gmail.com")
