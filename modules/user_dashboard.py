import streamlit as st
from modules.transactions import check_availability, issue_book, return_book

def user_dashboard(db):
    st.title("👤 User Dashboard")
    st.caption("Access: Reports + Transactions only (No Maintenance)")

    tabs = st.tabs(["🔎 Search Books", "✅ Issue Book", "↩️ Return Book"])

    with tabs[0]:
        check_availability(db)

    with tabs[1]:
        issue_book(db)

    with tabs[2]:
        return_book(db)
