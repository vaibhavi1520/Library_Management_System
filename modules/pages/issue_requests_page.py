import streamlit as st

def issue_requests_page(db):
    st.title("📝 Issue Requests")

    issues = db.get_active_issues()
    pending = issues[issues["returned"] == "No"]

    if pending.empty:
        st.info("No pending issue requests.")
        return

    st.dataframe(pending, use_container_width=True)
