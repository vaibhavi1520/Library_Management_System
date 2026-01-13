import streamlit as st
import plotly.express as px

def admin_reports(db):
    st.subheader("📊 Admin Reports")

    books = db.get_books()
    issues = db.get_active_issues()
    memberships = db.get_memberships()

    total_books = len(books)
    active_issues = len(issues[issues["returned"] == "No"])
    total_fines = db.total_fines_collected()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Books", total_books)
    c2.metric("Active Issues", active_issues)
    c3.metric("Total Fines Collected", f"₹{total_fines}")

    st.divider()

    
    fig = px.bar(
        books.groupby("category").size().reset_index(name="count"),
        x="category",
        y="count",
        title="Books by Category"
    )
    st.plotly_chart(fig, use_container_width=True)
