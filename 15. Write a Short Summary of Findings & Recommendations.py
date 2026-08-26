import pandas as pd

df = pd.read_csv("sales.csv")

print("========== FINDINGS ==========")

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

if "Category" in df.columns:
    category_sales = df.groupby("Category")["Sales"].sum()
    print("\nCategory-wise Sales:")
    print(category_sales)

    print("\nBest Category:")
    print(category_sales.idxmax())

if "Region" in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum()
    print("\nRegion-wise Sales:")
    print(region_sales)

    print("\nBest Region:")
    print(region_sales.idxmax())


print("\n========== RECOMMENDATIONS ==========")

print("1. Focus on high-performing categories.")
print("2. Increase marketing in high-performing regions.")
print("3. Monitor pricing and discount strategies.")
print("4. Use sales prediction for future planning.")
print("5. Improve the model by adding more relevant featuress.")
