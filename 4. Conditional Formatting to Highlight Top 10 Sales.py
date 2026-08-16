import pandas as pd

df = pd.read_excel("sales.xlsx")

# Find top 10 sales
top_10 = df.nlargest(10, "Sales")

print("Top 10 Sales:")
print(top_10)