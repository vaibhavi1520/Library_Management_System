import streamlit as st
from datetime import datetime
from modules.utils import compute_fine

def pay_fine_page(db):
    st.title("💰 Pay Fine")

    issues = db.get_active_issues()
    active = issues[issues["returned"] == "No"]

    issue_id = st.selectbox("Select Issue ID", active["issue_id"].tolist())
    row = active[active["issue_id"] == issue_id].iloc[0]

    today = datetime.today().date()
    fine = compute_fine(row["return_date"], today)

    st.write("### Fine Details")
    st.json(row.to_dict())
    st.error(f"Fine Amount: ₹{fine}")

    if st.button("Pay & Continue"):
        st.session_state["txn"]["step"] = "pay_fine"
        st.session_state["txn"]["data"] = {"issue_id": issue_id, "fine": fine}
        st.session_state["page"] = "confirmation"
        st.rerun()
