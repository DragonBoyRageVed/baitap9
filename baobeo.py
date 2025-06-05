import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="Interactive Charts", layout="wide")

st.title("📊 Interactive Charts and Map in Streamlit")

# --- Data generation ---
st.sidebar.header("Chart Settings")

# Bar chart data
bar_categories = ["Category A", "Category B", "Category C", "Category D"]
bar_values = np.random.randint(10, 100, size=len(bar_categories))
bar_df = pd.DataFrame({"Category": bar_categories, "Value": bar_values})

# Line chart data
line_x = pd.date_range(start="2024-01-01", periods=30)
line_y = np.random.randn(30).cumsum()
line_df = pd.DataFrame({"Date": line_x, "Value": line_y})

# Map data
num_points = st.sidebar.slider("Number of map points", 10, 100, 50)
map_data = pd.DataFrame({
    'lat': np.random.normal(loc=37.76, scale=0.01, size=num_points),
    'lon': np.random.normal(loc=-122.4, scale=0.01, size=num_points)
})

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Bar Chart")
    st.bar_chart(bar_df.set_index("Category"))

with col2:
    st.subheader("📈 Line Chart")
    st.line_chart(line_df.set_index("Date"))

st.subheader("🗺️ Interactive Map")
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=map_data,
            get_position="[lon, lat]",
            get_radius=100,
            get_color=[255, 0, 0, 140],
            pickable=True,
        ),
    ],
))





