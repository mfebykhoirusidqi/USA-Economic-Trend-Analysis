"""
Professional Streamlit Dashboard
US Economic Trend Analysis (2020–2025)
Author: M Feby Khoiru Sidqi |  GitHub : https://github.com/mfebykhoirusidqi/USA-Economic-Trend-Analysis

Features:
 - Interactive time-range filter
 - Multi-indicator Plotly charts (GDP, Inflation, Unemployment, Interest Rate, S&P 500)
 - Rolling averages, correlations, linear trend & short projection
 - Data table and CSV download
 - Built-in 'Theory / Interpretation' section for portfolio presentation
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
from sklearn.linear_model import LinearRegression  # small dependency useful for projection

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title=" USA Economic Trends Dashboard (2020-2025)",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------
# Utilities & Data
# -------------------------
@st.cache_data
def load_dummy_data():
    # Create realistic monthly dummy data for 2020-2025
    rng = pd.date_range("2020-01-01", "2025-12-31", freq="ME")
    np.random.seed(42)

    # Base trends (annualized / smoothed)
    months = np.arange(len(rng))
    # Simulated GDP (quarterly-ish growth but monthly interpolation)
    gdp_base = 21.0 + (months / 12) * 0.8 + np.sin(months / 24) * 0.3
    gdp_noise = np.random.normal(0, 0.1, size=len(rng))
    gdp = np.round(gdp_base + gdp_noise, 2)  # Trillion USD (smoothed)

    # Inflation: spike around 2021-2022 then gradual decline to 2025
    inflation_base = 1.8 + 0.8 * np.tanh((months - 24) / 18) + 0.3 * np.sin(months / 6)
    inflation = np.round(np.clip(inflation_base + np.random.normal(0, 0.15, size=len(rng)), 0.5, 8.0), 2)

    # Unemployment: high in 2020, then lowers
    unemployment_base = 8.5 - 4.0 * (1 / (1 + np.exp(-(months - 6) / 12)))  # decreases after 2020
    unemployment = np.round(np.clip(unemployment_base + np.random.normal(0, 0.2, size=len(rng)), 2.5, 12.0), 2)

    # Interest rate: low in 2020, rising 2022-2023, moderate in 2024-2025
    ir_base = 0.25 + 0.05 * np.tanh((months - 30) / 10) + 0.02 * np.sin(months / 10)
    interest_rate = np.round(np.clip(ir_base * 4.0, 0.0, 6.0), 2)  # scaled to realistic % levels

    # S&P 500: general upward trend with noise
    sp_base = 3200 + months * 5 + np.sin(months / 3) * 40
    sp = np.round(sp_base + np.random.normal(0, 40, len(rng)), 0)

    df = pd.DataFrame({
        "Date": rng,
        "GDP_trillion_USD": gdp,
        "Inflation_pct": inflation,
        "Unemployment_pct": unemployment,
        "InterestRate_pct": interest_rate,
        "SP500_index": sp
    })
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    return df

df = load_dummy_data()

# -------------------------
# Sidebar controls
# -------------------------
st.sidebar.header("Controls")
years = sorted(df["Year"].unique())
year_min, year_max = st.sidebar.select_slider(
    "Select year range",
    options=years,
    value=(2023, 2025),
)

indicators = st.sidebar.multiselect(
    "Select indicators to display",
    options=["GDP_trillion_USD", "Inflation_pct", "Unemployment_pct", "InterestRate_pct", "SP500_index"],
    default=["GDP_trillion_USD", "Inflation_pct", "SP500_index"]
)

rolling_window = st.sidebar.slider("Rolling average window (months)", min_value=1, max_value=12, value=3)
show_corr = st.sidebar.checkbox("Show correlation matrix", value=True)
projection_months = st.sidebar.number_input("Projection horizon (months)", min_value=0, max_value=24, value=6)

# -------------------------
# Filter data
# -------------------------
df_filtered = df[(df["Year"] >= year_min) & (df["Year"] <= year_max)].reset_index(drop=True)

st.sidebar.markdown("---")
st.sidebar.markdown("**Export / Download**")
if st.sidebar.button("Download filtered CSV"):
    csv = df_filtered.to_csv(index=False)
    st.sidebar.download_button("Download CSV", csv, file_name="us_economic_filtered.csv", mime="text/csv")
