import streamlit as st

from data.dummy_loader import load_dummy_data
from modules.db import MockDatabase
from modules.auth import admin_login, user_login
from modules.user_dashboard import user_dashboard
from modules.admin_dashboard import admin_dashboard
from modules.pages.transactions_page import transactions_page
from modules.pages.issue_requests_page import issue_requests_page
from modules.pages.pay_fine_page import pay_fine_page
from modules.pages.confirmation_page import confirmation_page
from modules.pages.user_management_page import user_management_page


st.set_page_config(page_title="Library Management System", layout="wide")


def init_state():
    if "page" not in st.session_state:
        st.session_state["page"] = "select_login"
    if "auth_role" not in st.session_state:
        st.session_state["auth_role"] = None

    
    if "db" not in st.session_state:
        books, memberships, issues, fines = load_dummy_data()
        st.session_state["db"] = MockDatabase(books, memberships, issues, fines)


def logout():
    st.session_state["auth_role"] = None
    st.session_state["page"] = "select_login"
    st.success("Logged out ✅")
    st.rerun()


def main():
    init_state()
    db = st.session_state["db"]

    
    st.sidebar.title("📚 LMS Navigation")
    if st.session_state["auth_role"]:
        st.sidebar.success(f"Logged in as: {st.session_state['auth_role'].upper()}")
        st.sidebar.button("Logout", on_click=logout)

    
    page = st.session_state["page"]

    if page == "select_login":
        st.title("📖 Library Management System")
        st.caption("Enterprise Modular Streamlit App")

        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                admin_login()

        with col2:
            with st.container(border=True):
                user_login()

    elif page == "admin_dashboard" and st.session_state["auth_role"] == "admin":
        admin_dashboard(db)

    elif page == "user_dashboard" and st.session_state["auth_role"] == "user":
        user_dashboard(db)
    
    elif page == "transactions":
        transactions_page(db)
    
    elif page == "issue_requests":
        issue_requests_page(db)
    
    elif page == "pay_fine":
        pay_fine_page(db)

    elif page == "confirmation":
        confirmation_page()

    elif page == "user_management":
        user_management_page()

    else:
        st.error("Unauthorized access or invalid route.")
        st.session_state["page"] = "select_login"
        st.rerun()


if __name__ == "__main__":
    main()
