import streamlit as st
from modules.transactions_flow import init_transaction

def transactions_page(db):
    st.title("🔎 Search Result – Book Issue")

    init_transaction()

    books = db.get_books()
    q = st.text_input("Search by Book Name / Author / Category")

    if q:
        q = q.lower()
        books = books[
            books["title"].str.lower().str.contains(q) |
            books["author"].str.lower().str.contains(q) |
            books["category"].str.lower().str.contains(q)
        ]

    st.dataframe(books, use_container_width=True)

    st.divider()
    st.subheader("📘 Issue Request")

    with st.form("issue_form"):
        membership_no = st.text_input("Membership ID")
        book_id = st.text_input("Book ID")
        submit = st.form_submit_button("Proceed")

        if submit:
            st.session_state["txn"]["step"] = "confirm"
            st.session_state["txn"]["data"] = {
                "membership_no": membership_no,
                "book_id": book_id
            }
            st.session_state["page"] = "confirmation"
            st.rerun()
