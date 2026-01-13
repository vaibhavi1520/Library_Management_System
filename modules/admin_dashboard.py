import streamlit as st
from modules.reports import admin_reports

def admin_maintenance(db):
    st.subheader("🛠 Maintenance Module (Mandatory)")

    tab1, tab2, tab3 = st.tabs(["📚 Books", "🪪 Memberships", "👤 Users (Mock)"])

    with tab1:
        st.write("### Add / Update Book")

        books = db.get_books()
        st.dataframe(books, use_container_width=True)

        with st.expander("➕ Add Book"):
            book_id = st.text_input("Book ID")
            title = st.text_input("Title")
            author = st.text_input("Author")
            category = st.text_input("Category")
            if st.button("Add Book"):
                if not all([book_id, title, author, category]):
                    st.error("All fields are mandatory")
                else:
                    db.add_book({
                        "book_id": book_id,
                        "title": title,
                        "author": author,
                        "category": category,
                        "available": "Yes"
                    })
                    st.success("Book added ✅")
                    st.rerun()

        with st.expander("✏️ Update Book"):
            selected_book = st.selectbox("Select Book ID", books["book_id"].tolist())
            new_available = st.selectbox("Available?", ["Yes", "No"])
            if st.button("Update Book Availability"):
                db.set_book_availability(selected_book, new_available)
                st.success("Updated ✅")
                st.rerun()

    with tab2:
        st.write("### Add / Update Membership")
        mem = db.get_memberships()
        st.dataframe(mem, use_container_width=True)

        with st.expander("➕ Add Membership"):
            membership_no = st.text_input("Membership No")
            name = st.text_input("Member Name")
            mtype = st.radio("Membership Duration", ["6 months", "1 year", "2 years"], index=0)
            if st.button("Add Membership"):
                if not all([membership_no, name]):
                    st.error("All fields mandatory")
                else:
                    db.add_membership({
                        "membership_no": membership_no,
                        "name": name,
                        "type": mtype,
                        "status": "Active"
                    })
                    st.success("Membership Added ✅")
                    st.rerun()

        with st.expander("✏️ Update Membership"):
            selected_mem = st.selectbox("Membership No", mem["membership_no"].tolist())
            action = st.radio("Action", ["Extend (6 months default)", "Cancel Membership"])
            if st.button("Confirm Membership Update"):
                if action.startswith("Extend"):
                    db.update_membership(selected_mem, {"type": "6 months"})
                    st.success("Membership Extended ✅")
                else:
                    db.update_membership(selected_mem, {"status": "Inactive"})
                    st.success("Membership Cancelled ✅")
                st.rerun()

    with tab3:
        st.info("User management can be extended using a User Master sheet (future scope).")

def admin_dashboard(db):
    st.title("👨‍💼 Admin Dashboard")

    nav = st.sidebar.radio("Admin Navigation", ["Reports", "Maintenance"])

    if nav == "Reports":
        admin_reports(db)
    else:
        admin_maintenance(db)
