import pandas as pd

df = pd.read_csv("data.csv")

# Sort by Category and Revenue
sorted_data = df.sort_values(
    by=["Category", "Revenue"],
    ascending=[True, False]
)

print(sorted_data)