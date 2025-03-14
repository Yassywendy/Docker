import os
import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

# Variables d'environnement pour la connexion à PostgreSQL
DATABASE_URL = os.getenv('DATABASE_URL')

# Créer une connexion à PostgreSQL
engine = create_engine(DATABASE_URL)

# Charger les données
query = "SELECT * FROM users"
df = pd.read_sql(query, engine)

# Afficher les données dans Streamlit
st.title("Données ETL")
st.write("Voici les données chargées depuis PostgreSQL :")
st.dataframe(df)