import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import os

st.set_page_config(page_title="COP32 Climate Dashboard", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    path = 'data/'  # Adjust if running from root
    files = glob.glob(os.path.join(path, "*_clean.csv"))
    all_df = []
    for f in files:
        df = pd.read_csv(f)
        df['Country'] = os.path.basename(f).split('_')[0].capitalize()
        all_df.append(df)
    full_df = pd.concat(all_df, ignore_index=True)
    full_df['Date'] = pd.to_datetime(full_df['Date'])
    full_df['Year'] = full_df['Date'].dt.year
    return full_df

df = load_data()

# --- SIDEBAR WIDGETS ---
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=df['Country'].unique())
year_range = st.sidebar.slider("Select Year Range", int(df['Year'].min()), int(df['Year'].max()), (2015, 2026))
variable = st.sidebar.selectbox("Select Variable", ["T2M", "PRECTOTCORR", "RH2M", "T2M_MAX"])

# Filter Logic
mask = (df['Country'].isin(countries)) & (df['Year'].between(year_range[0], year_range[1]))
filtered_df = df[mask]

# --- MAIN UI ---
st.title("🌍 African Climate Trend Analysis (COP32)")
st.markdown("This dashboard provides data-driven evidence for regional climate vulnerability.")

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Average {variable} Trend")
    # Aggregating for a smoother line chart
    trend_df = filtered_df.groupby(['Year', 'Country'])[variable].mean().reset_index()
    fig_line = px.line(trend_df, x='Year', y=variable, color='Country', markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader(f"{variable} Distribution (Boxplot)")
    fig_box = px.box(filtered_df, x='Country', y=variable, color='Country')
    st.plotly_chart(fig_box, use_container_width=True)

# KPI Metric Row
st.divider()
st.subheader("Key Vulnerability Indicators")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
kpi_col1.metric("Max Temperature", f"{filtered_df['T2M_MAX'].max()} °C")
kpi_col2.metric("Avg Rainfall", f"{filtered_df['PRECTOTCORR'].mean():.2f} mm")
kpi_col3.metric("Data Points", len(filtered_df))