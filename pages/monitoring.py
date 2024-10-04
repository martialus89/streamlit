import streamlit as st
import requests

st.set_page_config(
    page_title="M O N I T O R I N G",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


conn = sqlite3.connect('dbmodel.db')
cursor = conn.cursor()
# Récupérer les données de la table
cursor.execute(f'SELECT distinct model_name FROM model')
rows = cursor.fetchall()
cursor.close()
conn.close()
st.sidebar.selectbox('Choisissez votre modèle', [rows])


histo = st.checkbox("Voir l'historique des conversations")
if histo:
    r=requests.get('https://36e8-34-16-180-130.ngrok-free.app/read_table?table=model')
    r.text
    st.write(r.text)

retrain = st.checkbox("Réentrainement du model")
if retrain:
    list_model = requests.get('https://3d92-34-16-180-130.ngrok-free.app/model')
    list_model.text
    st.write(list_model.text)

metrics = st.checkbox("Voir les metrics d'un modèle")
if metrics:
    st.write("metrics!")