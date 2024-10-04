import streamlit as st

st.set_page_config(
    page_title="M O N I T O R I N G",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.selectbox('Choisissez votre modèle', ['Model 1', 'Model 2', 'Model 3'])

histo = st.checkbox("Voir l'historique des conversations")
if histo:
    st.write("histo!")

retrain = st.checkbox("Réentrainement du model")
if retrain:
    st.write("retrain !")

metrics = st.checkbox("Voir les metrics d'un modèle")
if metrics:
    st.write("metrics!")