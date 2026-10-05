import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model():
    # Load dataset
    df = pd.read_csv('transactions.csv')
    
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model to disk
    with open('fraud_model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    print("Model trained and saved as 'fraud_model.pkl'!")

if __name__ == '__main__':
    train_and_save_model()
