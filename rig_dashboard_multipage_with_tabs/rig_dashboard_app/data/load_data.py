import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/Updated_Merged_Data_with_API_and_Location.csv")
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
    # Rename back for consistency with original script
    df.rename(columns={
        "well_name": "Well_Name",
        "hole_size": "Hole_Size",
        "flowline_shakers": "flowline_Shakers",
        "operator": "Operator",
        "contractor": "Contractor"
    }, inplace=True)
    return df
