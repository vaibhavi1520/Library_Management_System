import streamlit as st

def active_issues_page(db):
    st.title("📌 Active Issues")

    issues = db.get_active_issues().copy()
    issues = issues[issues["returned"] == "No"]

    if issues.empty:
        st.info("No active issues currently.")
        return

    st.dataframe(issues, use_container_width=True)
