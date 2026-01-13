import streamlit as st


EXCEL_MENU = [
    ("📊 Reports", "reports"),
    ("📚 Master List of Books", "books_master"),
    ("🎬 Master List of Movies", "movies_master"),
    ("🪪 Master List of Memberships", "memberships_master"),
    ("📌 Active Issues", "active_issues"),
    ("⏰ Overdue returns", "overdue_returns"),
    ("🔎 Transactions (Search/Issue)", "transactions"),
    ("📝 Issue Requests", "issue_requests"),
    ("💰 Pay Fine", "pay_fine"),
    ("👤 User Management", "user_management"),
    ("🖼️ Reference Images", "reference_images"),
]


def sidebar_excel_navigation():
    st.sidebar.title("🟩 LMS Navigation")

    role = st.session_state.get("auth_role")
    if role:
        st.sidebar.success(f"Logged in as: {role.upper()}")

    st.sidebar.divider()

    # Excel style menu items
    for label, page in EXCEL_MENU:
        # user restriction (optional)
        if page == "user_management" and role != "admin":
            continue

        if st.sidebar.button(label, use_container_width=True):
            st.session_state["page"] = page
            st.rerun()

    st.sidebar.divider()

    # Bottom Controls (Home / Logout like Excel)
    col1, col2 = st.sidebar.columns(2)

    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state["page"] = "home_admin" if role == "admin" else "home_user"
            st.rerun()

    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state["auth_role"] = None
            st.session_state["user"] = None
            st.session_state["page"] = "select_login"
            st.rerun()
