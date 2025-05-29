
import streamlit as st
from data.load_data import load_well_data
from components.filter_bar import filter_controls

st.set_page_config(page_title="Rig Dashboard", layout="wide", page_icon="🛢️")

st.title("🛢️ Drilling Performance Dashboard")

df = load_well_data()
if not df.empty and "well_name" in df.columns and "rig" in df.columns:
    filter_controls(df["well_name"].unique(), df["rig"].unique())

    selected_well = st.session_state.get("selected_well")
    if selected_well:
        st.success(f"Selected Well: {selected_well}")
        st.dataframe(df[df["well_name"] == selected_well])
    else:
        st.info("No well selected.")
else:
    st.error("Required columns 'well_name' and 'rig' not found.")
