import streamlit as st

st.set_page_config(
  page_title="FullstackGPT Home",
  page_icon="ㅁ",
)

st.title("title")

# st.sidebar.title("sidebar title")

# st.sidebar.text_input("xxx")


with st.sidebar:
  st.title("sidebar title")
  st.text_input("xxx")
  
  
tab_a, tab_b = st.tabs(["a", "b"])

with tab_a:
  st.write("aaa")
  
with tab_b:
  st.write("bbb")