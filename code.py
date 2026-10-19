import numpy as np
import pandas as pd

df = pd.read_csv("demo.csv")

df["pf"] = df["salary"] * 0.06

print(df)
df.dropna(inplace=True)

# df.to_excel("final.xlsx", index=False)
df.to_csv("final.csv", index=False)

df.to_json("output.json")