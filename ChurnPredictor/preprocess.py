# preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    df_clean = df.copy()
    label_encoders = {}

    categorical_cols = ['gender', 'location', 'contract_type', 'payment_method']
    for col in categorical_cols:
        encoder = LabelEncoder()
        df_clean[col] = encoder.fit_transform(df_clean[col])
        label_encoders[col] = encoder

    X = df_clean.drop(['customer_id', 'churned'], axis=1)
    y = df_clean['churned']

    return X, y, label_encoders
