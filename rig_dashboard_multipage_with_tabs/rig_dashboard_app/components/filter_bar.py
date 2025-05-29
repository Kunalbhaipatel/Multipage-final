import streamlit as st

def render_filters(df):
    st.markdown("Use filters to explore well-level, shaker-type, and fluid performance metrics.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        operator = st.selectbox("Select Operator", ["All"] + sorted(df["Operator"].dropna().unique().tolist()))
    with col2:
        temp = df if operator == "All" else df[df["Operator"] == operator]
        contractor = st.selectbox("Select Contractor", ["All"] + sorted(temp["Contractor"].dropna().unique().tolist()))
    with col3:
        temp = temp if contractor == "All" else temp[temp["Contractor"] == contractor]
        shaker = st.selectbox("Select Shaker", ["All"] + sorted(temp["flowline_Shakers"].dropna().unique().tolist()))
    with col4:
        temp = temp if shaker == "All" else temp[temp["flowline_Shakers"] == shaker]
        hole = st.selectbox("Select Hole Size", ["All"] + sorted(temp["Hole_Size"].dropna().unique().tolist()))

    temp = temp if hole == "All" else temp[temp["Hole_Size"] == hole]
    return temp
