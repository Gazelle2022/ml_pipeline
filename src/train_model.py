import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump
import os

DATA_PATH = "data/dataset.csv"
MODEL_PATH = "model/model.pkl"

def train_model():
    df = pd.read_csv(DATA_PATH)
    if df.shape[1] < 2:
        print("Pas assez de colonnes pour entraîner le modèle.")
        return
    X = df.iloc[:, 1].values.reshape(-1, 1)
    y = df.iloc[:, 0].values
    model = LinearRegression()
    model.fit(X, y)
    os.makedirs("model", exist_ok=True)
    dump(model, MODEL_PATH)
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()
