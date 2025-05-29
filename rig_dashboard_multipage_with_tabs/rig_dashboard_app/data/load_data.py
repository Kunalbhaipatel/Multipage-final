import pandas as pd
import os
import streamlit as st

@st.cache_data
def load_data():
    csv_path = os.path.join("data", "Updated_Merged_Data_with_API_and_Location.csv")
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()  # clean up leading/trailing spaces
        df.rename(columns={
            "Well_Name": "well_name",
            "flowline_Shakers": "shaker",
            "Operator": "operator",
            "Contractor": "contractor",
            "Hole_Size": "hole_size",
        }, inplace=True)
        return df
    except Exception as e:
        st.error(f"Could not load CSV: {e}")
        return pd.DataFrame()
