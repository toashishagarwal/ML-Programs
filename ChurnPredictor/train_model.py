# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier
import joblib
from data_generator import generate_full_dataset
from preprocess import preprocess
from evaluate import plot_confusion

def train_churn_model():
    # Load or generate data
    df = generate_full_dataset(1000)

    # Preprocess
    X, y, label_encoders = preprocess(df)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model training
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "churn_model.pkl")
    print("\n✅ Model saved as churn_model.pkl")
    plot_confusion(y_test, y_pred)

if __name__ == "__main__":
    train_churn_model()
