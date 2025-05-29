
import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    try:
        path = os.path.join(os.path.dirname(__file__), "..", "sample_rig_dashboard_data.csv")
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        aliases = {
            "well": "well_name",
            "well_name": "well_name",
            "rig": "rig",
            "rig_name": "rig"
        }
        df.rename(columns=aliases, inplace=True)

        return df
    except Exception as e:
        st.error(f"❌ CSV Load Error: {e}")
        return pd.DataFrame(columns=["well_name", "rig"])
