import joblib
import pandas as pd

# Load model
model = joblib.load("data/models/salary_model.pkl")

# Sample input
sample = pd.DataFrame({
    'title': ['Data Scientist'],
    'location': ['New York']
})

# Predict salary
sample['title'] = sample['title'].astype('category').cat.codes
sample['location'] = sample['location'].astype('category').cat.codes
prediction = model.predict(sample)
print("Predicted Salary:", prediction[0])
