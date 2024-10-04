import streamlit as st
import requests
import sqlite3

st.set_page_config(
    page_title="M O N I T O R I N G",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

histo = st.checkbox("Voir l'historique des conversations")
if histo:
    r=requests.get('https://36e8-34-16-180-130.ngrok-free.app/read_table?table=model')
    r.text
    st.write(r.text)

retrain = st.checkbox("Réentrainement du model")
if retrain:
    list_model = requests.get('https://3d92-34-16-180-130.ngrok-free.app/model')
    list_model.text
    options = [row[1] for row in list_model]
    st.sidebar.selectbox('Choisissez votre modèle', options)

metrics = st.checkbox("Voir les metrics d'un modèle")
if metrics:
    st.write("metrics!")