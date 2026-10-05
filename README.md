# AI-Powered Fraud Detection & Transaction Risk Scorer

🚀 **Live Demo:** [fraud-detecter.onrender.com](https://fraud-detecter.onrender.com)

## Overview
This repository contains a full-stack, machine learning-powered transaction risk scoring service designed to evaluate banking transactions in real-time. The project demonstrates practical data science, model serialization, and backend API development using Python, Scikit-Learn, and Flask.

---

## Key Features
* **Synthetic Data Generation:** Simulates realistic financial transaction behavior with controlled fraud indicators (`generate_data.py`).
* **Machine Learning Classification:** Trains a Random Forest Classifier to assess risk patterns (`model.py`).
* **REST API Backend:** Exposes a lightweight Flask endpoint (`/predict`) to score incoming transaction payloads instantaneously (`app.py`).

---

## Project Structure
* **`generate_data.py`** - Script to generate synthetic transaction datasets with feature distributions.
* **`model.py`** - Handles data splitting, model training, performance evaluation, and `.pkl` serialization.
* **`app.py`** - Flask web server providing the real-time scoring API endpoint.
* **`fraud_model.pkl`** - The serialized trained machine learning model.
* **`transactions.csv`** - The underlying dataset used for training.
* **`requirements.txt`** - Project dependencies and libraries.

---

## Getting Started & Local Setup

### Prerequisites
* Python 3.x installed on your system.

### Installation & Execution
1. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com/fanele2022/Fraud-Detecter.git
   cd Fraud-Detecter
   ```

2. Install the required dependencies:
   ```bash
   python3 -m pip install pandas scikit-learn flask
   ```

3. Generate the training data:
   ```bash
   python3 generate_data.py
   ```

4. Train and serialize the machine learning model:
   ```bash
   python3 model.py
   ```

5. Launch the Flask API server:
   ```bash
   python3 app.py
   ```

---

## Testing the API
You can test the live prediction endpoint using `curl` from your terminal:

```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"amount": 450.0, "hour": 2, "distance": 75.5, "is_international": 1}'
```

### Sample JSON Response:
```json
{
  "fraud_predicted": false,
  "fraud_risk_score": 31.0
}
```

---

## Author
* **Fanele Magubane**
