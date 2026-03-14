import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- LOGIN CHECK ---------------- #

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# ---------------- PAGE TITLE ---------------- #

st.title("Country Comparison")

# ---------------- LOAD DATA ---------------- #

df = pd.read_csv("data/inequality_data.csv")

df.columns = df.columns.str.strip().str.lower()

# ---------------- COUNTRY SELECT ---------------- #

col1, col2 = st.columns(2)

with col1:
    c1 = st.selectbox("Country 1", sorted(df["country"].unique()))

with col2:
    c2 = st.selectbox("Country 2", sorted(df["country"].unique()))

# ---------------- FILTER DATA ---------------- #

data = df[df["country"].isin([c1, c2])]

# ---------------- PLOT ---------------- #

fig = px.line(
    data,
    x="year",
    y="gini_index",
    color="country",
    markers=True,
    title="Inequality Comparison"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- DATA TABLE ---------------- #

st.subheader("Comparison Data")

st.dataframe(data)