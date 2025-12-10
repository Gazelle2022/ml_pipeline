import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

def train_model():
    df = pd.read_csv("data/cleaned_dataset.csv")

    X = df.drop("month", axis=1)
    y = df["month"]

    # Encode categorical target
    le = LabelEncoder()
    y = le.fit_transform(y)

    model = LinearRegression()
    model.fit(X, y)

    print("Model trained successfully")
    return model
