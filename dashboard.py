import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Job Market Analyzer")
st.write("Analyzing 14,000+ data from 2024")

df=pd.read_csv("jobs_in_data_2024.csv")

#sidebar filters 
st.sidebar.header ('Filters')
experience = st.sidebar.multiselect(
    "Experience Level",
    options =df['experience_level'].unique(),
    default =df['experience_level'].unique()
)

work_setting = st.sidebar.multiselect(
    "Work Setting",
    options=df['work_setting'].unique(),
    default=df['work_setting'].unique()
    )

company_size =st.sidebar.multiselect(
    "Company Size",
    options = df['company_size'].unique(),
    default =df['company_size'].unique()
)

#Apply fitlers 
filtered_df=df[
    (df['experience_level'].isin(experience)) &
    (df['work_setting'].isin(work_setting)) &
    (df['company_size'].isin(company_size))
    
]

st.write (f"showing {len(filtered_df)} of {len(df)} jobs")

col1,col2,col3 =st.columns(3)
col1.metric("Average Salary",f"${filtered_df['salary_in_usd'].mean():,.0f}")
col2.metric("Median Salary",f"${filtered_df['salary_in_usd'].median():,.0f}")
col3.metric("Total Jobs",f"{len(filtered_df):,}")

st.subheader("Average Salary by Experience Level")
fig,ax =plt.subplots()
exp_salary =filtered_df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending =False)
exp_salary.plot(kind='bar',color='steelblue',ax=ax)
ax.set_xlabel("Experience level")
ax.set_ylabel("Average Salary (USD)")
plt.tight_layout ()
st.pyplot(fig)
plt.close()

#top 10 highest paying jobs(from your analysis)

st.subheader("Top 10 highest paying jobs")
fig,ax=plt.subplots()
top_jobs=filtered_df.groupby('job_title')['salary_in_usd'].mean().sort_values (ascending=False).head(10)
top_jobs.plot(kind='barh', color ='red', ax=ax)
ax.set_xlabel("Average salary (USD)")
ax.set_ylabel("Job Title")
plt.tight_layout()
st.pyplot(fig)
plt.close()

#slary trend over the years 

st.subheader("Salary Trend Over The Years")
fig,ax = plt.subplots()
yearly_salary= filtered_df.groupby('work_year')['salary_in_usd'].mean()
yearly_salary.plot(kind ='line',color='green',ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Average Salary (USD)')
plt.tight_layout()
st.pyplot(fig)
plt.close()

#work setting Pie chart 

st.subheader("Jobs by work setting")
fig,ax =plt.subplots()
filtered_df['work_setting'].value_counts().plot(kind='pie',autopct= '%1.1f%%', ax=ax)
ax.set_ylabel("")
plt.tight_layout()
st.pyplot(fig)
plt.close()

#jobs by category

st.subheader("jobs by category")
fig,ax =plt.subplots()
filtered_df['job_category'].value_counts().plot(kind='barh',color='purple',ax=ax)
ax.set_xlabel('Number of Jobs')
ax.set_ylabel('Job Category')
plt.tight_layout()
st.pyplot(fig)
plt.close()


st.subheader("Raw Data")
st.dataframe(filtered_df)
