import pandas as pd

df = pd.read_csv("data.csv")

total_revenue = df.groupby("Category")["Revenue"].sum()

print(total_revenue)