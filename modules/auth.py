import streamlit as st

ADMIN_CREDENTIALS = {"username": "adm", "password": "adm"}

USER_CREDENTIALS = {
    "user": "user"
}

def admin_login():
    st.subheader("🔐 Admin Login")

    u = st.text_input("Username", key="admin_username")
    p = st.text_input("Password", type="password", key="admin_password")

    if st.button("Login as Admin", key="admin_login_btn"):
        if u == "adm" and p == "adm":
            st.session_state["auth_role"] = "admin"
            st.session_state["page"] = "admin_dashboard"
            st.success("Welcome Admin ✅")
            st.rerun()
        else:
            st.error("Invalid Admin Credentials")


def user_login():
    st.subheader("🔐 User Login")

    u = st.text_input("Username", key="user_username")
    p = st.text_input("Password", type="password", key="user_password")

    if st.button("Login as User", key="user_login_btn"):
        if u in USER_CREDENTIALS and USER_CREDENTIALS[u] == p:
            st.session_state["auth_role"] = "user"
            st.session_state["page"] = "user_dashboard"
            st.success("Login Success ✅")
            st.rerun()
        else:
            st.error("Invalid User Credentials")

