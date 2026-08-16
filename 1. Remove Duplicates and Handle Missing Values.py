import pandas as pd

df = pd.read_csv("sales.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

print(df)