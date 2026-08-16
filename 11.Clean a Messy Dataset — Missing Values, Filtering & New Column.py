import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# 1. Handle missing values
df = df.fillna(0)

# 2. Filter rows
# Example: keep rows where Sales is greater than 1000
filtered_df = df[df["Sales"] > 1000]

# 3. Create a new column
# Example: calculate Profit
df["Profit"] = df["Sales"] - df["Cost"]

# Display cleaned dataset
print(df)

# Display filtered data
print("\nFiltered Data:")
print(filtered_df)