import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Inequality Platform", layout="wide")

# ---------------- SESSION ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ---------------- #

if not st.session_state.logged_in:

    st.markdown(
        "<h1 style='text-align:center;'>🌍 Global Inequality Analytics Platform</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>User Login</h3>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            try:
                df = pd.read_csv("data/users.csv")

                user = df[
                    (df["username"] == username) &
                    (df["password"] == password)
                ]

                if not user.empty:

                    st.session_state.logged_in = True
                    st.success("Login successful")
                    st.rerun()

                else:
                    st.error("Invalid username or password")

            except:
                st.error("User database not found")

        st.divider()

        st.write("Don't have an account?")

        if st.button("Signup"):
            st.switch_page("pages/Signup.py")

    st.stop()

# ---------------- HOME PAGE ---------------- #

st.title("Welcome to Global Inequality Platform")

st.write("""
Use the **sidebar** to explore the platform.

Available features include:

- Income Inequality Dashboard
- Country Analysis
- Country Comparison
- Global Trend Analysis
- Decade Comparison
- Country Forecasting
- AI Insights with PDF Report

This platform helps analyze global income inequality using interactive visualizations.
""")

# ---------------- LOGOUT ---------------- #

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()