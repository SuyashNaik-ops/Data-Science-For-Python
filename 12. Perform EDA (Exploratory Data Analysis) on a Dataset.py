import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

# Basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Numerical columns
print("\nCorrelation Matrix:")
print(df.select_dtypes(include="number").corr())

# Sales distribution
if "Sales" in df.columns:
    df["Sales"].hist()
    plt.title("Sales Distribution")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()