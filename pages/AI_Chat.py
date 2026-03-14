import streamlit as st
import pandas as pd

st.title("AI Data Assistant")

df = pd.read_csv("data/inequality_data.csv")

question = st.text_input("Ask a question about inequality data")

if question:

    q = question.lower()

    if "highest" in q or "most inequality" in q:
        country = df.sort_values("Gini_Index",ascending=False).iloc[0]
        st.write(
            f"The country with the highest inequality is {country['Country']} "
            f"with a Gini Index of {country['Gini_Index']}."
        )

    elif "lowest" in q:
        country = df.sort_values("Gini_Index").iloc[0]
        st.write(
            f"The country with the lowest inequality is {country['Country']} "
            f"with a Gini Index of {country['Gini_Index']}."
        )

    elif "average" in q:
        avg = df["Gini_Index"].mean()
        st.write(f"The average global Gini Index is {round(avg,2)}.")

    elif "gini" in q:
        st.write(
            "The Gini Index measures income inequality. "
            "Higher values mean more inequality."
        )

    else:
        st.write(
            "Sorry, I can answer questions about inequality trends, "
            "highest/lowest countries, and Gini index."
        )