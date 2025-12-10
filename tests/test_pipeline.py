from src.update_data import download_data, clean_data
from src.train_model import train_model
import os

def test_pipeline():
    # 1. Créer le dossier data si nécessaire
    if not os.path.exists("data"):
        os.makedirs("data")

    # 2. Télécharger et nettoyer les données
    download_data()    # crée data/raw_dataset.csv
    clean_data()       # crée data/cleaned_dataset.csv

    # 3. Vérifier que le fichier existe avant de lancer le modèle
    assert os.path.exists("data/cleaned_dataset.csv"), "cleaned_dataset.csv n'existe pas !"

    # 4. Entraîner le modèle
    train_model()

