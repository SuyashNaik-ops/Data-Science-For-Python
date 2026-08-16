import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("sales.csv")

# Remove rows with missing values
df = df.dropna()

# Select features and target
features = ["Price", "Quantity", "Discount"]
target = "Sales"

X = df[features]
y = df[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict sales
y_pred = model.predict(X_test)

# Evaluate model
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Compare actual and predicted values
result = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred
})

print("\nActual vs Predicted Sales:")
print(result.head(10))