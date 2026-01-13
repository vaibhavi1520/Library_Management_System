import streamlit as st
from modules.transactions_flow import reset_transaction

def confirmation_page():
    st.title("✅ Confirmation")

    txn = st.session_state.get("txn", {})

    st.write("### Transaction Summary")
    st.json(txn.get("data", {}))

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✔ Confirm"):
            st.success("Transaction Completed Successfully")
            reset_transaction()
            st.session_state["page"] = "reports"
            st.rerun()

    with col2:
        if st.button("❌ Cancel"):
            st.warning("Transaction Cancelled")
            reset_transaction()
            st.session_state["page"] = "reports"
            st.rerun()
