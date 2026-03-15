import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Login", layout="centered")

# SESSION
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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

        users_file = "data/users.csv"

        if os.path.exists(users_file):

            df = pd.read_csv(users_file)

            if "username" in df.columns and "password" in df.columns:

                user = df[(df["username"] == username) & (df["password"] == password)]

                if not user.empty:
                    st.session_state.logged_in = True
                    st.success("Login successful")

                    st.switch_page("pages/Home.py")

                else:
                    st.error("Invalid username or password")

            else:
                st.error("users.csv format incorrect")

        else:
            st.error("User database not found")

    st.divider()

    st.write("Don't have an account?")

    if st.button("Signup"):
        st.switch_page("pages/Signup.py")
