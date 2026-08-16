import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")

# Create Excel report
with pd.ExcelWriter("Final_Sales_Report.xlsx") as writer:

    # Cleaned data
    df.to_excel(
        writer,
        sheet_name="Dataset",
        index=False
    )

    # Summary statistics
    df.describe().to_excel(
        writer,
        sheet_name="Statistics"
    )

    # Category-wise sales
    if "Category" in df.columns and "Sales" in df.columns:
        df.groupby("Category")["Sales"].sum().to_excel(
            writer,
            sheet_name="Category Sales"
        )

    # Region-wise sales
    if "Region" in df.columns and "Sales" in df.columns:
        df.groupby("Region")["Sales"].sum().to_excel(
            writer,
            sheet_name="Region Sales"
        )

    # Correlation
    df.select_dtypes(include="number").corr().to_excel(
        writer,
        sheet_name="Correlation"
    )

print("Final Excel report created successfully.")