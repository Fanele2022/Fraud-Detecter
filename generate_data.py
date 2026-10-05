import pandas as pd
import numpy as np

def generate_synthetic_transactions(num_samples=1000):
    np.random.seed(42)
    
    amounts = np.random.exponential(scale=100.0, size=num_samples) # Most transactions are small, some are large
    hours = np.random.randint(0, 24, size=num_samples)
    distances = np.random.exponential(scale=10.0, size=num_samples) # Distance from home in km
    is_international = np.random.choice([0, 1], size=num_samples, p=[0.9, 0.1])
    
    # Define a rule for fraud (high amount + far distance + international + odd hours)
    fraud_score = (
        (amounts > 300).astype(int) * 2 +
        (distances > 50).astype(int) * 3 +
        is_international * 3 +
        ((hours < 5) | (hours > 23)).astype(int) * 2 +
        np.random.normal(0, 1, size=num_samples)
    )
    
    # Classify top risk scores as fraud (1) else legitimate (0)
    classes = (fraud_score > 6).astype(int)
    
    df = pd.DataFrame({
        'Amount': amounts,
        'Hour': hours,
        'Distance': distances,
        'Is_International': is_international,
        'Class': classes
    })
    
    df.to_csv('transactions.csv', index=False)
    print("Dataset 'transactions.csv' generated successfully!")

if __name__ == '__main__':
    generate_synthetic_transactions()