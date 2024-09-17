import streamlit as st

with st.form("my_form"):
  st.write("my_form")
  name = st.text_input("Your name ?")

  #every form must have a submit button
  submitted = st.form_submit("Submit")
  if submitted:
    st.write(f"Hi {name}")

