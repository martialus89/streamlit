import streamlit as st
import pandas as pd

st.title("My dashboard")
df = pd.read_csv('data.csv')
st.write(df)
