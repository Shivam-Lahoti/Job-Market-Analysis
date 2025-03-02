from flask import Flask , request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load Model
model= joblib.load("data/models/salary_model.pkl")

@app.route('/predict', methods= ['POST'])
def predict():
    data = request.json
    sample = pd.DataFrame(data)
    sample['title'] = sample['title'].astype('category').cat.codes
    sample['location'] = sample['location'].astype('category').cat.codes
    prediction = model.predict(sample)
    return jsonify({'predicted_salary': prediction[0]})


if __name__ =='__main__':
    app.run(debu=True)

