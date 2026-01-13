import streamlit as st

def memberships_master_page(db):
    st.title("🪪 Master List of Memberships")

    mem = db.get_memberships().copy()
    st.dataframe(mem, use_container_width=True)

    st.divider()

    tab1, tab2 = st.tabs(["➕ Add Membership", "✏️ Update Membership"])

    with tab1:
        with st.form("add_membership_form"):
            membership_no = st.text_input("Membership Id")
            name = st.text_input("Name of Member")
            contact_no = st.text_input("Contact Number")
            address = st.text_area("Contact Address")
            aadhar = st.text_input("Aadhar Card No")
            status = st.selectbox("Status", ["Active", "Inactive"])
            mtype = st.selectbox("Membership Type", ["6 months", "1 year", "2 years"])

            submitted = st.form_submit_button("Confirm")
            if submitted:
                db.add_membership({
                    "membership_no": membership_no,
                    "name": name,
                    "type": mtype,
                    "status": status,
                })
                st.success("Membership Added ✅")
                st.rerun()

    with tab2:
        mem_ids = mem["membership_no"].tolist()
        selected = st.selectbox("Select Membership Id", mem_ids)
        new_status = st.selectbox("Update Status", ["Active", "Inactive"])
        if st.button("Confirm Update"):
            db.update_membership(selected, {"status": new_status})
            st.success("Membership Updated ✅")
            st.rerun()
