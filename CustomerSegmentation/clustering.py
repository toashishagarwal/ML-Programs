# src/clustering.py
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import joblib
import os
from src.config import BASE_DIR

MODEL_PATH = os.path.join(BASE_DIR, 'models')
os.makedirs(MODEL_PATH, exist_ok=True)

def train_kmeans(df, k=4):
    features = ['recency', 'frequency', 'monetary', 'age', 'income']
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=k, random_state=42)
    df['segment'] = model.fit_predict(X_scaled)
    
     # Save scaler and model
    joblib.dump(scaler, os.path.join(MODEL_PATH, 'scaler.pkl'))
    joblib.dump(model, os.path.join(MODEL_PATH, 'kmeans_model.pkl'))

    print(f"✅ Saved model and scaler to {MODEL_PATH}")
    
    return df
