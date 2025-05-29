from data_loader import load_data

df = load_data()
import streamlit as st
st.title("📄 Well Overview")
st.markdown("This page will show detailed metrics by well, matching the original dashboard's layout.")
