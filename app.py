import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ✅ This must be the first Streamlit command
st.set_page_config(
    layout='wide',
    page_title="India Census 2011",
    page_icon="📊"
)

# Title
st.title("📊 India State-Level Data Visualization")

# Load Data
df = pd.read_csv('final_df.csv')

# Sidebar
st.sidebar.title("🇮🇳 India Ka Data")

# State selector
list_states = df['State'].unique().tolist()
list_states.insert(0, 'overall india')
selected_state = st.sidebar.selectbox('Select State', list_states)

# Parameter selectors
primary = st.sidebar.selectbox("Select Primary Parameter (Size)", sorted(df.columns[6:20]))
secondary = st.sidebar.selectbox("Select Secondary Parameter (Color)", sorted(df.columns[6:20]))

# Plot button
if st.sidebar.button("Plot"):
    st.markdown("**🟢 Size represents:** {}".format(primary))
    st.markdown("**🔵 Color represents:** {}".format(secondary))

    # Filter Data
    data_to_plot = df if selected_state == 'overall india' else df[df['State'] == selected_state]

    # Create Map
    fig = px.scatter_mapbox(
        data_to_plot,
        lat="Latitude",
        lon="Longitude",
        size=primary,
        color=secondary,
        zoom=4 if selected_state == 'overall india' else 5,
        size_max=35,
        mapbox_style="carto-darkmatter",  # Try "open-street-map", "stamen-terrain", etc.
        width=1200,
        height=700,
        hover_name='District'
    )

    st.plotly_chart(fig, use_container_width=True)
