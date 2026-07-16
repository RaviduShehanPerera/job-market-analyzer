import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("jobs_in_data_2024.csv")

#salary by experience level
#print(f"columns: {df.columns.tolist()}")

grp_experiencelevel = df.groupby('experience_level')['salary_in_usd'].mean().sort_values (ascending=False)
#print(grp_experiencelevel)
grp_experiencelevel.plot(kind='bar',color='blue')
plt.title('Salary by Experience Level')
plt.xlabel('Experience')
plt.ylabel('Average Salary (USD)')
plt.tight_layout()
plt.savefig("salary_by_experience.png", dpi=150)
plt.close()


#top 10 highest paying job titles 
grp_jobtitle = df.groupby('job_title')['salary_in_usd'].mean().sort_values (ascending=False).head(10).round(2)
#print(grp_jobtitle)
grp_jobtitle.plot(kind='barh', color='red')
plt.title('Top 10 Highest Paying Job')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Job Title')
plt.tight_layout()
plt.savefig("top10_jobs.png", dpi=150)
plt.close()


#jobs by work setting 
#print(df['work_setting'].value_counts())
df['work_setting'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Jobs by Work Setting')
plt.tight_layout()
plt.savefig("work_setting.png", dpi=150)
plt.close()


#Average salary by company size
print(df.columns.tolist())
grp_companysize = df.groupby('company_size')['salary_in_usd'].mean().sort_values (ascending = False).round(2)
grp_companysize.plot(kind ='bar', color='blue')
plt.title('Average Salary by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig("salary_by_company_size.png", dpi=150)
plt.close()

#salary trend over the years 
grp_workyear=df.groupby('work_year')['salary_in_usd'].mean().round(0)
grp_workyear.plot(kind='line',color='green')
plt.title('Salary Trend Over Years')
plt.xlabel('work_year')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig("salary_trend.png", dpi=150)
plt.close()



