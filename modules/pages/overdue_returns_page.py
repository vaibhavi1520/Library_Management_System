import streamlit as st
from datetime import datetime

def overdue_returns_page(db):
    st.title("⏰ Overdue Returns")

    issues = db.get_active_issues().copy()
    issues = issues[issues["returned"] == "No"]
    if issues.empty:
        st.info("No active issues.")
        return

    today = datetime.today().date()
    overdue = issues[issues["return_date"] < today]

    if overdue.empty:
        st.success("No overdue returns ✅")
        return

    st.error(f"Overdue returns found: {len(overdue)}")
    st.dataframe(overdue, use_container_width=True)
