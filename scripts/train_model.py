import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
import joblib
import os

os.makedirs("data/models", exist_ok=True)


# Load cleaned data
df = pd.read_csv("data/cleaned/cleaned_jobs.csv")

# Feature engineering
df['location'] = df['location'].astype('category').cat.codes
df['title'] = df['title'].astype('category').cat.codes

# Train-test split
X = df[['title', 'location']]
y = df['salary'].fillna(df['salary'].mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print("RMSE:", root_mean_squared_error(y_test, predictions, squared=False))

# Save model
joblib.dump(model, "data/models/salary_model.pkl")
print("Model saved to data/models/salary_model.pkl")