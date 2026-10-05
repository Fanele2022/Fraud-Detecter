from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained modelS
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return jsonify({"message": "AI Fraud Detection API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    try:
        # Expecting JSON payload: {"amount": 450.0, "hour": 2, "distance": 75.5, "is_international": 1}
        features = np.array([[
            float(data['amount']),
            float(data['hour']),
            float(data['distance']),
            int(data['is_international'])
        ]])
        
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] # Probability of fraud
        
        result = {
            "fraud_predicted": bool(prediction),
            "fraud_risk_score": round(float(probability) * 100, 2)
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)