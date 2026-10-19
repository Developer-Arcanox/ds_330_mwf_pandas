import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Vishal", np.nan, "Kunal", np.nan, "Sumit", "Vishal"],
        "age": [34, 45, 56, 67, 78, 34],
        "salary": [56000, 34000, np.nan, 84000, 62000, 56000],
        "department": ["Sales", "Marketing", "Sales", "Finance", "Sales", "Finance"],
    }
)

print(df.isna())
print(df.isna().sum())

df = df.dropna(axis=0)
df.dropna(inplace=True)

df.fillna(0, inplace=True)

df["salary"] = df["salary"].fillna(0)

print(df)
df.info()

print(df.duplicated())

df.drop_duplicates(inplace=True)

print(df)

df_group = df.groupby("department").agg(
    {
        "salary": ["sum", "mean"],
        "age": "mean",
    }
)

print(df_group)

df.to_csv("demo.csv", index=False)

df.to_excel("example.xlsx", index=False)