import streamlit as st
import numpy as np

st.title("My final project")
st.subheader("My subtitle")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
