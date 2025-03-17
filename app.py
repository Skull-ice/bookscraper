import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Books to Scrape - Visualisation des données")

# Charger les données depuis le fichier CSV
df = pd.read_csv("all_books_to_scrape.csv")

# Afficher les données dans un tableau interactif
st.subheader("Tableau des livres")
st.dataframe(df)

# Ajouter un filtre par prix
st.subheader("Filtrer par prix")
min_price, max_price = st.slider(
    "Sélectionnez une plage de prix",
    float(df["Prix"].str.replace("£", "").astype(float).min()),
    float(df["Prix"].str.replace("£", "").astype(float).max()),
    (float(df["Prix"].str.replace("£", "").astype(float).min()), float(df["Prix"].str.replace("£", "").astype(float).max())),
)

# Appliquer le filtre
filtered_df = df[
    (df["Prix"].str.replace("£", "").astype(float) >= min_price) &
    (df["Prix"].str.replace("£", "").astype(float) <= max_price)
]

# Afficher les données filtrées
st.subheader("Livres filtrés par prix")
st.dataframe(filtered_df)

# Afficher un graphique de distribution des prix
st.subheader("Distribution des prix")
st.bar_chart(filtered_df["Prix"].str.replace("£", "").astype(float).value_counts())
