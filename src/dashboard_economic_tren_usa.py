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
    rng = pd.date_range("2020-01-01", "2025-12-31", freq="M")
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

st.sidebar.markdown("---")
st.sidebar.markdown("**Export / Download**")
if st.sidebar.button("Download filtered CSV"):
    csv = df_filtered.to_csv(index=False)
    st.sidebar.download_button("Download CSV", csv, file_name="us_economic_filtered.csv", mime="text/csv")

# -------------------------
# Filter data
# -------------------------
df_filtered = df[(df["Year"] >= year_min) & (df["Year"] <= year_max)].reset_index(drop=True)

# -------------------------
# Header / Top metrics
# -------------------------
st.title("USA Economic Trends Dashboard (Portfolio Demo) By M Feby Khoiru Sidqi")
st.markdown("Interactive analysis of macroeconomic indicators. This dashboard is built "
            "for portfolio demonstration—showing data wrangling, analytics, visualization, "
            "and interpretation skills suitable for data or economics roles.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Average GDP (Trillion USD)", f"{df_filtered['GDP_trillion_USD'].mean():.2f}")
col2.metric("Average Inflation (%)", f"{df_filtered['Inflation_pct'].mean():.2f}%")
col3.metric("Average Unemployment (%)", f"{df_filtered['Unemployment_pct'].mean():.2f}%")
col4.metric("Avg Interest Rate (%)", f"{df_filtered['InterestRate_pct'].mean():.2f}%")

st.markdown("---")

# -------------------------
# Time series chart (multi-indicator) - Plotly
# -------------------------
fig = go.Figure()
yaxes = {
    "GDP_trillion_USD": {"title": "GDP (Trillion USD)", "side": "left", "overlaying": None},
    "Inflation_pct": {"title": "Inflation (%)", "side": "right", "overlaying": "y"},
    "Unemployment_pct": {"title": "Unemployment (%)", "side": "right", "overlaying": "y"},
    "InterestRate_pct": {"title": "Interest Rate (%)", "side": "right", "overlaying": "y"},
    "SP500_index": {"title": "S&P 500 Index", "side": "right", "overlaying": "y"}
}

# Add selected indicators to the plot with different y-axes where appropriate
for ind in indicators:
    if ind == "GDP_trillion_USD":
        fig.add_trace(go.Scatter(x=df_filtered["Date"], y=df_filtered[ind], mode="lines+markers",
                                 name="GDP (Trillions USD)", yaxis="y1", line=dict(width=2)))
    elif ind == "SP500_index":
        fig.add_trace(go.Scatter(x=df_filtered["Date"], y=df_filtered[ind], mode="lines+markers",
                                 name="S&P 500", yaxis="y2", line=dict(width=2, dash="dot")))
    else:
        fig.add_trace(go.Scatter(x=df_filtered["Date"], y=df_filtered[ind], mode="lines+markers",
                                 name=ind.replace("_", " "), yaxis="y2", opacity=0.9))

# Layout with 2 y-axes
fig.update_layout(
    xaxis_title="Date",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(l=40, r=40, t=80, b=40),
    template="plotly_white",
)

# configure a second y-axis if SP500 or percentages are present
fig.update_layout(
    yaxis=dict(title="GDP (Trillion USD)"),
    yaxis2=dict(title="Percent / Index", overlaying="y", side="right")
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Rolling average and small table
# -------------------------
st.subheader("Rolling Average & Recent Values")
df_roll = df_filtered.copy()
for ind in indicators:
    df_roll[f"{ind}_roll"] = df_roll[ind].rolling(window=rolling_window, min_periods=1).mean()

st.dataframe(df_roll[["Date"] + [c for c in df_roll.columns if c.endswith("_roll")]].tail(12), height=240)

# -------------------------
# Correlation matrix
# -------------------------
if show_corr:
    st.subheader("Correlation Matrix (Selected Indicators)")
    corr_df = df_filtered[["GDP_trillion_USD", "Inflation_pct", "Unemployment_pct", "InterestRate_pct", "SP500_index"]].corr()
    fig_corr = px.imshow(corr_df, text_auto=True, aspect="auto", color_continuous_scale="RdYlBu_r")
    st.plotly_chart(fig_corr, use_container_width=True)

# -------------------------
# Trend projection (simple linear regression on GDP)
# -------------------------
if projection_months > 0:
    st.subheader("GDP Short Projection (Linear Trend)")
    # Use month index as X for regression
    df_proj = df_filtered.reset_index().rename(columns={"index": "month_index"})
    X = df_proj[["month_index"]].values
    y = df_proj["GDP_trillion_USD"].values
    model = LinearRegression()
    model.fit(X, y)

    # Build future index and predictions
    last_index = df_proj["month_index"].iloc[-1]
    future_idx = np.arange(last_index + 1, last_index + 1 + projection_months)
    X_future = future_idx.reshape(-1, 1)
    y_future = model.predict(X_future)

    # Show projection chart
    fig_proj = go.Figure()
    fig_proj.add_trace(go.Scatter(x=df_filtered["Date"], y=df_filtered["GDP_trillion_USD"],
                                  name="Actual GDP", mode="lines+markers"))
    future_dates = pd.date_range(df_filtered["Date"].iloc[-1] + pd.offsets.MonthEnd(1), periods=projection_months, freq="M")
    fig_proj.add_trace(go.Scatter(x=future_dates, y=y_future, name=f"Projection (+{projection_months} months)",
                                  mode="lines", line=dict(dash="dash", color="red")))
    fig_proj.update_layout(title="GDP: Actual vs Linear Projection", xaxis_title="Date", yaxis_title="GDP (Trillion USD)",
                           template="plotly_white")
    st.plotly_chart(fig_proj, use_container_width=True)

    # Display short numeric summary
    last_actual = df_filtered["GDP_trillion_USD"].iloc[-1]
    proj_end = y_future[-1]
    pct_change = (proj_end - last_actual) / last_actual * 100
    st.markdown(f"**Projection summary:** last actual GDP = {last_actual:.2f}T USD → projected after {projection_months} months = {proj_end:.2f}T USD ({pct_change:.2f}% change)")

# -------------------------
# Data table and download
# -------------------------
st.subheader("Underlying Data (Filtered)")
st.dataframe(df_filtered, height=260)

csv_buffer = StringIO()
df_filtered.to_csv(csv_buffer, index=False)
st.download_button(label="Download filtered data (CSV)", data=csv_buffer.getvalue(), file_name="us_economic_filtered.csv", mime="text/csv")

# -------------------------
# Theory / Economic Interpretation (Portfolio-ready text)
# -------------------------
st.markdown("---")
st.header("Theory & Economic Interpretation")
st.markdown(
    """
    **Why these indicators matter**  
    - **GDP (Gross Domestic Product)**: broadest measure of aggregate economic activity. Persistent positive GDP growth indicates expansion.  
    - **Inflation**: increases in the general price level; central banks (e.g., the Federal Reserve) may raise interest rates to cool high inflation.  
    - **Unemployment**: lagging indicator of labor-market health. Falling unemployment typically indicates economic recovery, but very low levels can press wages and inflation.  
    - **Interest Rate**: policy tool used to manage inflation and economic growth. Rate hikes slow growth and reduce inflationary pressures; cuts stimulate activity.

    **Typical relationships**  
    - Inflation ↔ Interest Rate: central banks tend to increase nominal rates when inflation is above target.  
    - GDP ↔ Unemployment: generally inverse (Okun's law): as GDP grows, unemployment tends to fall.  
    - Equity markets (S&P 500) may rise during growth but are sensitive to rate policy and inflation surprises.

    **How to interpret the dashboard**  
    - Use the time-range slider to focus on specific periods (e.g., inflation spike, rate hikes).  
    - Rolling averages help remove short-term noise and show underlying trends.  
    - Correlation matrix provides quick checks for co-movement; causality is not implied.  
    - Linear projection is a simple statistical baseline — for production forecasting, prefer ARIMA, Prophet, or structural models.

    This content is intentionally concise for portfolio presentation. You can expand each subsection into a notebook or README section to demonstrate domain knowledge during interviews.
    """
)

st.markdown("---")
st.caption("Dashboard generated for portfolio demonstration. Replace dummy data with real data extraction (PDF / API) to showcase end-to-end ETL + analytics.")
