from data_loader import load_data

df = load_data()
import streamlit as st

st.title("📈 Summary Charts")
st.markdown("Charts summarizing performance across key drilling KPIs.")
