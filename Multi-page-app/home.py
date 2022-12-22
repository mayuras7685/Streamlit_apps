import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Home page! 👋")

st.sidebar.success("Select from above pages")

st.markdown("This is Multi page streamlit app")