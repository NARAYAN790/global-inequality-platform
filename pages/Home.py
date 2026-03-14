import streamlit as st
import pandas as pd

st.title("GLOBAL INEQUALITY PLATFORM")

df = pd.read_csv("data/inequality_data.csv")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Countries Tracked", df["Country"].nunique())
c2.metric("Average Inequality", round(df["Gini_Index"].mean(), 2))
c3.metric("Years Covered", df["Year"].nunique())
c4.metric("Data Points", len(df))

st.subheader("Quick Actions")

a1, a2, a3, a4 = st.columns(4)

a1.button("Explore Data")
a2.button("Country Compare")
a3.button("View Trends")
a4.button("AI Insights")