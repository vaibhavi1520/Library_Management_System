import streamlit as st

def user_management_page():
    st.title("👤 User Management")

    tab1, tab2 = st.tabs(["➕ Add User", "✏ Update User"])

    with tab1:
        with st.form("add_user"):
            name = st.text_input("Name")
            is_admin = st.checkbox("Admin")
            active = st.checkbox("Active", value=True)
            if st.form_submit_button("Confirm"):
                st.success("User Added (Mock)")

    with tab2:
        st.info("User update logic can be extended with DB / CSV later.")
