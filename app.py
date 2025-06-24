import streamlit as st
import streamlit.components.v1 as components

with open("reef.html", "r", encoding='utf-8') as f:
    html_content = f.read()

components.html(html_content, height=2000, scrolling=True)