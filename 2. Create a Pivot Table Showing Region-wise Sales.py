import pandas as pd

df = pd.read_csv("sales.csv")

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    aggfunc="sum"
)

print(pivot)