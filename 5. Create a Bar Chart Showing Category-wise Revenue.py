import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")

# Calculate category-wise revenue
revenue = df.groupby("Category")["Revenue"].sum()

# Create bar chart
revenue.plot(kind="bar")

plt.title("Category-wise Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()