import streamlit as st
import pandas as pd

st.title("My dashboard")
st.subheader("My subtitle")

df = pd.read_csv('data.csv', sep=';')

if st.checkbox("print jeu de données"):
  st.write(df)

ville=df.ville.unique()
user_selection = st.selectbox('Select une ville',ville)
st.write(df[df.ville == user_selection])


