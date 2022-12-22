import streamlit as st


st.set_page_config(
    page_title="2nd Page",
    page_icon=":two:",
)

st.write("# Welcome to Second page! 👋")

st.sidebar.header("Second Page")

st.markdown("This is second page content")