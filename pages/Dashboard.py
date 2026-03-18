import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

st.title("📊 Global Inequality Dashboard")

df = pd.read_csv("data/inequality_data.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Countries Tracked", df["Country"].nunique())
col2.metric("Average Gini Index", round(df["Gini_Index"].mean(), 2))
col3.metric("Latest Year", df["Year"].max())

st.divider()

st.subheader("📈 Income Inequality by Country")
fig = px.bar(df, x="Country", y="Gini_Index")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📉 Inequality Trend Over Time")
fig2 = px.line(df, x="Year", y="Gini_Index", color="Country")
st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("🌐 Power BI Dashboard")

st.markdown(
    '<iframe width="100%" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiYzEwNGVmZDYtODdjNy00NWQ4LWIzYzAtMmExYzlkZjUzMGVjIiwidCI6IjhmYWQ5NzYxLWZhZGItNDFiNi04YTFkLWRjMDVkNWRjNGY5YiJ9"></iframe>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("📄 Dataset Preview")
st.dataframe(df)
