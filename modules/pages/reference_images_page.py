import streamlit as st

def reference_images_page():
    st.title("🖼️ Reference Excel UI Screenshots")

    st.info("These images are for UI reference, matching Excel flow.")

    tab1, tab2, tab3 = st.tabs(["Reports UI", "Membership UI", "User Management UI"])

    with tab1:
        st.image("assets/excel_reports.png", use_container_width=True)

    with tab2:
        st.image("assets/excel_memberships.png", use_container_width=True)

    with tab3:
        st.image("assets/excel_user_management.png", use_container_width=True)
