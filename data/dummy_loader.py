import pandas as pd
from datetime import datetime, timedelta

def load_dummy_data():
    
    books = pd.DataFrame([
        {"book_id": "B001", "title": "Clean Code", "author": "Robert C. Martin", "category": "Programming", "available": "Yes"},
        {"book_id": "B002", "title": "Deep Learning", "author": "Ian Goodfellow", "category": "AI/ML", "available": "Yes"},
        {"book_id": "B003", "title": "Python Crash Course", "author": "Eric Matthes", "category": "Programming", "available": "No"},
        {"book_id": "B004", "title": "Atomic Habits", "author": "James Clear", "category": "Self-help", "available": "Yes"},
        {"book_id": "B005", "title": "The Pragmatic Programmer", "author": "Andy Hunt", "category": "Programming", "available": "Yes"},
    ])

    memberships = pd.DataFrame([
        {"membership_no": "M001", "name": "Vaibhavi", "type": "1 year", "status": "Active"},
        {"membership_no": "M002", "name": "Rahul Sharma", "type": "6 months", "status": "Active"},
        {"membership_no": "M003", "name": "Neha Verma", "type": "2 years", "status": "Inactive"},
    ])

    
    issues = pd.DataFrame([
        {
            "issue_id": "I001",
            "membership_no": "M001",
            "book_id": "B003",
            "title": "Python Crash Course",
            "author": "Eric Matthes",
            "serial_no": "S1001",
            "issue_date": (datetime.today() - timedelta(days=10)).date(),
            "return_date": (datetime.today() + timedelta(days=5)).date(),
            "returned": "No",
            "fine": 0
        }
    ])

    fine_payments = pd.DataFrame(columns=[
        "payment_id", "issue_id", "membership_no", "book_id", "amount", "paid_date"
    ])

    return books, memberships, issues, fine_payments
