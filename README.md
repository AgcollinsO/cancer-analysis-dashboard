# 🧬 Cancer Data Analysis Dashboard

This project is an **interactive data analysis dashboard** built with **Streamlit** to explore cancer-related insights using a synthetic dataset. It aims to uncover trends and patterns in treatment cost, survival years, severity, and lifestyle impacts.

![Global Cancer Analysis Screenshoot1](https://github.com/user-attachments/assets/9d4668b7-2233-4e79-84ad-61ca123a352f)

---

🎯 **Live App**: [Launch Streamlit Dashboard](https://cancer-analysis-dashboard-57tfh5fasjeenahqvd5b3e.streamlit.app/)

✍️ **Medium Article**: [Read the full write-up on Medium](https://medium.com/@collinsobinna68/title-uncovering-patterns-in-global-cancer-data-a-visual-analytics-approach-2015-2024-8203f8b6ed38)

🔗 **LinkedIn Post**: [See project announcement on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7349430965791793152/) 

👤 **Author Profile**: [Agwu Collins Obinna – LinkedIn](https://www.linkedin.com/in/agwu-collins-90087b366)

---


## 📊 Key Features

- **Trend Analysis:** Yearly trend of cancer cases
- **Treatment Costs:** Average cost by country, stage, and cancer type
- **Survival Analysis:** Comparison across cancer stages and age groups
- **Lifestyle Impact:** Correlation of smoking, alcohol use, and obesity with survival and severity
- **Severity Drivers:** Multivariate correlation to identify what contributes most to high severity
- **Healthcare Gap:** Identify regions with high severity but low treatment costs

- ## 🚀 Live Demo
[Launch on Streamlit Cloud]([https://cancer-analysis-dashboard.streamlit.app](https://cancer-analysis-dashboard-57tfh5fasjeenahqvd5b3e.streamlit.app/)) 

## 📁 Project Structure
- `app.py` – main Streamlit app
- `global_cancer_patients_2015_2024.csv` – cleaned dataset
- `requirements.txt` – dependencies
- `main project codes.ipynb` – exploratory analysis

## 📊 Insights & Findings
- A line chart showed a steady increase in global cancer cases from 2015 to 2024.
- Certain cancer types, particularly Liver, Pancreatic, Brain, Lung, and Esophageal — are associated with significantly higher average treatment expenses.
- Advanced cancer stages typically require more aggressive and prolonged therapy.
- Patients aged 0–20 had the highest average survival years post-diagnosis, while patients aged 81+ had the lowest.
---

## 🧪 Future Improvements
- Add country-specific deep dives
- Integrate additional datasets (e.g., air quality, GDP)
- Add user-upload feature for custom datasets

## 🧠 Hypotheses Tested

1. Patients with advanced cancer stages have lower survival years.
2. Higher genetic risk scores are linked to higher severity scores.
3. Smoking and alcohol use negatively impact survival years.
4. Treatment costs are higher for more severe cases.
5. Gender affects treatment costs and survival.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Matplotlib / Seaborn**
- **Streamlit**
- **Git & GitHub**

---

## 👤 Author
**Agwu Collins Obinna**  
📧 collinsobinna68@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/agwu-collins-90087b366)

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/AgcollinsO/cancer-analysis-dashboard.git
   cd cancer-dashboard
