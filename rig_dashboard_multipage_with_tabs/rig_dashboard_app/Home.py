import streamlit as st
from components.filter_bar import render_filters
from data.load_data import load_data
df = load_data()

st.set_page_config(layout="wide", page_title="Rig Comparison Dashboard", page_icon="📊")

# Header
st.markdown("""
<style>
.header { background-color: #1c1c1c; padding: 1rem 2rem; color: white; font-size: 1.8rem; font-weight: bold; }
</style>
<div class='header'>📊 Rig Comparison Dashboard <span style='float:right; font-size:0.9rem;'>Powered by ProdigyIQ</span></div>
""", unsafe_allow_html=True)

# Load and filter data
df = load_data()
filtered = render_filters(df)

# Metrics section
st.markdown("### 📈 Key Performance Metrics")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Avg Total Dilution", f"{filtered['Total_Dil'].mean():,.2f} BBLs")
with m2:
    st.metric("Avg SCE", f"{filtered['Total_SCE'].mean():,.2f}")
with m3:
    st.metric("Avg DSRE", f"{filtered['DSRE'].mean()*100:.1f}%")
