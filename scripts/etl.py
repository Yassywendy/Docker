import os
import pandas as pd
from sqlalchemy import create_engine

# Variables d'environnement pour la connexion à PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL')

# Créer une connexion à PostgreSQL
engine = create_engine(DATABASE_URL)

# Extraction : Exemple de données simulées
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}
df = pd.DataFrame(data)

# Transformation : Ajouter une colonne
df["age_group"] = df["age"].apply(lambda x: "Young" if x < 30 else "Adult")

# Chargement : Insérer dans la base PostgreSQL
df.to_sql("users", engine, if_exists="replace", index=False)

print("ETL terminé, données insérées dans PostgreSQL.")
