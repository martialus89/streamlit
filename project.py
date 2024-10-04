import streamlit as st

st.set_page_config(
    page_title="projet",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

key = st.sidebar.text_input("Enter Ngrok key 👇")
if key:
        st.sidebar.write("You entered: ", key)