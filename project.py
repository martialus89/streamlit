import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

import streamlit as st

key = st.sidebar.text_input("Enter Ngrok key 👇")
if key:
        st.sidebar.write("You entered: ", key)