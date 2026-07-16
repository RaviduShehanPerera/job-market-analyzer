import pandas as pd

df = pd.read_csv("jobs_in_data_2024.csv")

print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nData types: \n{df.dtypes}")
print(f"\nMissing values:\n {df.isnull().sum()}")
print(f"\nSample job titles:\n {df['job_title'].value_counts().head(10)}")