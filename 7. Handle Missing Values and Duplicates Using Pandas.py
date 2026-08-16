import pandas as pd

df = pd.read_csv("data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

print(df)