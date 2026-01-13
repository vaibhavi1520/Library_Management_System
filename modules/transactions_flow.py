import streamlit as st

def init_transaction():
    if "txn" not in st.session_state:
        st.session_state["txn"] = {
            "step": "search",
            "data": {}
        }

def reset_transaction():
    st.session_state["txn"] = {
        "step": "search",
        "data": {}
    }
