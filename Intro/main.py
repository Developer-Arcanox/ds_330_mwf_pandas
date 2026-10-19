import numpy as np
import pandas as pd

# Series
# DataFrame

# s = pd.Series([34, 45, 56, 67, 78])
.

# print(s)
# print(s[0:3])

df = pd.DataFrame(
    {
        "Name": ["Amit", "Vishal", "Neeraj", "Kunal", "Ravi", "Yogesh"],
        "Age": [23, 34, 45, 56, 67, 78],
        "Salary": [34, 56, 67, 78, 23, 54],
    }
)

# print(df.tail(3))
# df.info()

# df.to_csv("data.csv", index=False)

df["HRA"] = df["Salary"] * 0.12

df["Net Salary"] = df["Salary"] + df["HRA"]


def checkAge(age):
    if age > 30:
        return "Above 30"
    else:
        return "Below 30"


df["Age Cat"] = df["Age"].apply(checkAge)

print(df)

# print(df.describe())
