import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("📊 India State-Level Data Visualization")
st.set_page_config(layout='wide')
df = pd.read_csv('final_df.csv')
list_states = df['State'].unique().tolist()
list_states.insert(0, 'overall india')

st.sidebar.title("India Ka Data")
selected_state = st.sidebar.selectbox('Select State', list_states)


primary = st.sidebar.selectbox("Enter first parameter", sorted(df.columns[6:20]))
secondary = st.sidebar.selectbox("Enter second parameter", sorted(df.columns[6:20]))

Plot = st.sidebar.button("Plot")

if Plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')

    if selected_state == 'overall india':
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=4,
            size_max=35,
            mapbox_style="carto-darkmatter",
            width=1200,
            height=700,
            hover_name='District'
        )
        st.plotly_chart(fig)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=5,
            size_max=35,
            mapbox_style="carto-darkmatter",
            width=1200,
            height=700,
            hover_name='District'
        )
        st.plotly_chart(fig)
