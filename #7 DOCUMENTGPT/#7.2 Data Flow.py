import streamlit as st
from datetime import datetime
today = datetime.today().strftime("%H:%M:%S")

model = st.selectbox("Choose", ("a", "b"))

st.title(today)

st.write(model)

if (model == "a"):
  st.write("aaa")
else:
  st.write("bbb") 

  name = st.text_input("what is your name")

  st.write(name)

  value = st.slider("temprature", min_value=1, max_value=10)

  st.write(value)