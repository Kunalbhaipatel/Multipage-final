import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    try:
        # Path to your CSV file
        path = os.path.join(os.path.dirname(__file__), "..", "sample_rig_dashboard_data.csv")
        df = pd.read_csv(path)

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Rename key fields to match expected filter names
        df.rename(columns={
            "contractor": "rig",         # Use contractor as rig
            "well_name": "well_name"     # Already normalized
        }, inplace=True)

        # Ensure required columns exist
        if "well_name" not in df.columns or "rig" not in df.columns:
            st.error("❌ Required columns 'well_name' and 'rig' not found after renaming.")
            return pd.DataFrame(columns=["well_name", "rig"])

        return df

    except Exception as e:
        st.error(f"❌ CSV Load Error: {e}")
        return pd.DataFrame(columns=["well_name", "rig"])
