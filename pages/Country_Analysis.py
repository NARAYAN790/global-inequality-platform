import streamlit as st
import pandas as pd
import plotly.express as px

# LOGIN CHECK
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

st.title("Country Inequality Analysis")

# LOAD DATA
df = pd.read_csv("data/inequality_data.csv")

df.columns = df.columns.str.strip().str.lower()

# COUNTRY SELECT
country = st.selectbox("Select Country", sorted(df["country"].unique()))

country_df = df[df["country"] == country]

st.subheader(f"Inequality Trend for {country}")

fig = px.line(
    country_df,
    x="year",
    y="gini_index",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("GDP vs Inequality")

fig2 = px.scatter(
    country_df,
    x="gdp",
    y="gini_index",
    size="top10_income_share",
    hover_data=["year"]
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Country Data")

st.dataframe(country_df)