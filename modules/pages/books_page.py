import streamlit as st

def books_master_page(db):
    st.title("📚 Master List of Books")

    books = db.get_books().copy()
    st.dataframe(books, use_container_width=True)

    st.divider()
    st.subheader("➕ Add Book")

    with st.form("add_book_form"):
        book_id = st.text_input("Book ID")
        title = st.text_input("Name of Book")
        author = st.text_input("Author Name")
        category = st.text_input("Category")
        status = st.selectbox("Status", ["Yes", "No"])
        cost = st.number_input("Cost", min_value=0, step=1)
        procurement_date = st.date_input("Procurement Date")

        submitted = st.form_submit_button("Confirm")
        if submitted:
            if not all([book_id, title, author, category]):
                st.error("All fields mandatory")
            else:
                db.add_book({
                    "book_id": book_id,
                    "title": title,
                    "author": author,
                    "category": category,
                    "available": status,
                })
                st.success("Book Added ✅")
                st.rerun()
