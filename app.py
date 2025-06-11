import streamlit as st

# ✅ Must be FIRST Streamlit command
st.set_page_config(
    layout='wide',
    page_title="India Census 2011",
    page_icon="📊"
)

import pandas as pd
import numpy as np
import plotly.express as px

# Title
st.title("📊 India State-Level Data Visualization")

# Load data
df = pd.read_csv('final_df.csv')

# Sidebar
st.sidebar.title("🇮🇳 India Ka Data")
list_states = df['State'].unique().tolist()
list_states.insert(0, 'overall india')

selected_state = st.sidebar.selectbox('Select State', list_states)
primary = st.sidebar.selectbox("Select Primary Parameter (Size)", sorted(df.columns[6:20]))
secondary = st.sidebar.selectbox("Select Secondary Parameter (Color)", sorted(df.columns[6:20]))

if st.sidebar.button("Plot"):
    st.markdown(f"**🟢 Size represents:** {primary}")
    st.markdown(f"**🔵 Color represents:** {secondary}")

    # Filter
    data = df if selected_state == 'overall india' else df[df['State'] == selected_state]

    # Plot
    fig = px.scatter_mapbox(
        data,
        lat="Latitude",
        lon="Longitude",
        size=primary,
        color=secondary,
        zoom=4 if selected_state == 'overall india' else 5,
        size_max=35,
        mapbox_style="carto-darkmatter",
        width=1200,
        height=700,
        hover_name='District'
    )

    st.plotly_chart(fig, use_container_width=True)
