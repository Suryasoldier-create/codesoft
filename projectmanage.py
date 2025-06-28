from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('priority_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([[data['deadline'], data['workload'], data['complexity'], data['progress']]])
    return jsonify({'priority': prediction[0]})

app.run(port=5000)
