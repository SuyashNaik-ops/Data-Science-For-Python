import pandas as pd

df = pd.read_csv("data.csv")

# Select numerical columns
numerical_data = df.select_dtypes(include="number")

# Create correlation matrix
correlation_matrix = numerical_data.corr()

print(correlation_matrix)