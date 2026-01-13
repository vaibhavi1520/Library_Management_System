import pandas as pd
from datetime import datetime, timedelta
import streamlit as st
from modules.utils import generate_id, compute_fine

def check_availability(db):
    st.subheader("📚 Book Availability Check")

    books = db.get_books().copy()
    query = st.text_input("Search Title / Author / Category")

    if query:
        q = query.lower()
        books = books[
            books["title"].str.lower().str.contains(q) |
            books["author"].str.lower().str.contains(q) |
            books["category"].str.lower().str.contains(q)
        ]

    st.dataframe(books, use_container_width=True)

def issue_book(db):
    st.subheader("✅ Book Issue")

    membership_no = st.text_input("Membership Number (Required)")
    book_id = st.text_input("Book ID (Required)")

    if not membership_no or not book_id:
        st.info("Enter Membership No and Book ID to proceed.")

    if st.button("Issue Book"):
        
        mem = db.get_memberships()
        if membership_no not in mem["membership_no"].values:
            st.error("Invalid Membership Number")
            return

        if mem.loc[mem["membership_no"] == membership_no, "status"].values[0] != "Active":
            st.error("Membership is not Active")
            return

        
        books = db.get_books()
        row = books[books["book_id"] == book_id]
        if row.empty:
            st.error("Book ID not found")
            return

        if row["available"].values[0] != "Yes":
            st.error("Book is not available currently")
            return

        issue_date = datetime.today().date()
        return_date_default = (datetime.today() + timedelta(days=15)).date()

        issue_id = generate_id("I", db.get_active_issues()["issue_id"].tolist())

        issue_row = {
            "issue_id": issue_id,
            "membership_no": membership_no,
            "book_id": book_id,
            "title": row["title"].values[0],
            "author": row["author"].values[0],
            "serial_no": generate_id("S", []),
            "issue_date": issue_date,
            "return_date": return_date_default,
            "returned": "No",
            "fine": 0
        }

        db.create_issue(issue_row)
        db.set_book_availability(book_id, "No")

        st.success(f"Book Issued ✅ Issue ID: {issue_id}")

def return_book(db):
    st.subheader("↩️ Return Book + Fine Payment")

    issues = db.get_active_issues()
    active_issues = issues[issues["returned"] == "No"]

    if active_issues.empty:
        st.info("No active issues pending return.")
        return

    selected_issue = st.selectbox("Select Issue ID", active_issues["issue_id"].tolist())
    issue_row = active_issues[active_issues["issue_id"] == selected_issue].iloc[0]

    st.write("### Issue Details")
    st.json(issue_row.to_dict())

    actual_return_date = st.date_input("Actual Return Date", value=datetime.today().date())

    fine = compute_fine(issue_row["return_date"], actual_return_date)

    st.info(f"Calculated Fine: ₹{fine}")

    fine_paid = st.checkbox("Fine Paid", value=(fine == 0))
    remarks = st.text_area("Remarks (Optional)")

    if st.button("Confirm Return"):
        if fine > 0 and not fine_paid:
            st.error("Fine is pending. Please mark Fine Paid before completing return.")
            return

        db.mark_returned(selected_issue, fine)
        db.set_book_availability(issue_row["book_id"], "Yes")

        if fine > 0:
            payment_row = {
                "payment_id": generate_id("P", db.fines_df["payment_id"].tolist() if not db.fines_df.empty else []),
                "issue_id": selected_issue,
                "membership_no": issue_row["membership_no"],
                "book_id": issue_row["book_id"],
                "amount": fine,
                "paid_date": datetime.today().date()
            }
            db.add_fine_payment(payment_row)

        st.success("Book Returned Successfully ✅")
        st.rerun()
