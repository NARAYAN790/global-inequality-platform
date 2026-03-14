import streamlit as st
import pandas as pd
import os

st.title("📝 Signup")

username = st.text_input("Create Username")
password = st.text_input("Create Password", type="password")

if st.button("Create Account"):

    if username == "" or password == "":
        st.warning("Please enter username and password")

    else:

        file_path = "data/users.csv"

        # अगर file नहीं है तो create करो
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["username","password"])
            df.to_csv(file_path,index=False)

        users = pd.read_csv(file_path)

        # duplicate check
        if username in users["username"].values:
            st.error("Username already exists")

        else:

            new_user = pd.DataFrame({
                "username":[username],
                "password":[password]
            })

            users = pd.concat([users,new_user],ignore_index=True)

            users.to_csv(file_path,index=False)

            st.success("Account created successfully!")
            st.info("Now go back to Login page and sign in.")