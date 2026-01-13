import streamlit as st
import plotly.express as px


def reports_page(db):
    st.title("📊 Reports / Dashboard")
    st.caption("Excel-style Chart / Reports page")

    books = db.get_books()
    issues = db.get_active_issues()
    memberships = db.get_memberships()

    total_books = len(books)
    active_issues = len(issues[issues["returned"] == "No"])
    total_memberships = len(memberships)
    total_fines = db.total_fines_collected()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📚 Total Books", total_books)
    c2.metric("📌 Active Issues", active_issues)
    c3.metric("🪪 Memberships", total_memberships)
    c4.metric("💰 Fines Collected", f"₹{total_fines}")

    st.divider()

    
    st.subheader("📈 Library Analytics")

    if books.empty:
        st.info("No books found in master list.")
        return

    
    if "category" not in books.columns:
        st.error("Missing column: category in books master list.")
        return

    category_df = books.groupby("category").size().reset_index(name="count")

    fig = px.bar(
        category_df,
        x="category",
        y="count",
        title="Books by Category",
        text="count",
    )
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Number of Books",
        title_x=0.4
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    
    tab1, tab2, tab3 = st.tabs(["📚 Books", "🪪 Memberships", "📌 Active Issues"])

    with tab1:
        st.dataframe(books, use_container_width=True)

    with tab2:
        st.dataframe(memberships, use_container_width=True)

    with tab3:
        active = issues[issues["returned"] == "No"]
        if active.empty:
            st.success("No active issues ✅")
        else:
            st.dataframe(active, use_container_width=True)
