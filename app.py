import streamlit as st

with open("reef.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=3000, scrolling=True)
