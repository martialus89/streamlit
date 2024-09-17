import streamlit as st

st.title("My dashboard")
st.subheader("My subtitle")

with st.form("my_form"):
  st.write("my_form")
  name = st.text_input("Your name ?")
  
  longitude = st.slider("Select un longitude", min_value=20, max_value=100, value=30, step=1)
  latitude = st.slider("Select un latitude", min_value=20, max_value=100, value=30, step=1)
  housing_median_age = st.slider("Select un housing_median_age", min_value=20, max_value=100, value=30, step=1)
  total_rooms = st.slider("Select un total_rooms", min_value=20, max_value=100, value=30, step=1)
  total_bedrooms = st.slider("Select un total_bedrooms", min_value=20, max_value=100, value=30, step=1)
  population = st.slider("Select un population", min_value=20, max_value=100, value=30, step=1)
  households = st.slider("Select un households", min_value=20, max_value=100, value=30, step=1)
  median_income = st.slider("Select un median_income", min_value=20, max_value=100, value=30, step=1)

  #every form must have a submit button
  submitted = st.form_submit("Submit")
  if submitted:
    st.write(f"Hi {name}")
    





# st.write(df[df.age == age_selection])


# {
#   "longitude": -114,
#   "latitude": 34.19,
#   "housing_median_age": 15.0,
#   "total_rooms": 5612.0,
#   "total_bedrooms": 1283.0,
#   "population": 1015.0,
#   "households": 472.0,
#   "median_income": 1.4936
# }





