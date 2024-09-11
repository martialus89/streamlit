import streamlit as st
import pandas as pd

st.title("My dashboard")
st.subheader("My subtitle")

df = pd.read_csv('data.csv', sep=';')

if st.checkbox("print jeu de données"):
  st.write(df)
