import streamlit as st

# LOGIN CHECK
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# PAGE CONTENT
st.title("About This Project")

st.markdown("""
### 🌍 Global Inequality Analytics Platform

This project analyzes **global income inequality** using interactive data visualizations.

### Tools Used
- Python
- Streamlit
- Pandas
- Plotly

### Features
- Global inequality dashboard
- Country comparison
- Trend analysis
- AI insights
- Data reports
""")