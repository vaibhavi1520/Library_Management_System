import pandas as pd
from datetime import datetime

class MockDatabase:
    """
    Mimics Excel sheets using DataFrames:
    - books_df
    - memberships_df
    - issues_df
    - fines_df
    """

    def __init__(self, books_df, memberships_df, issues_df, fines_df):
        self.books_df = books_df
        self.memberships_df = memberships_df
        self.issues_df = issues_df
        self.fines_df = fines_df

    
    def get_books(self):
        return self.books_df

    def add_book(self, row: dict):
        self.books_df = pd.concat([self.books_df, pd.DataFrame([row])], ignore_index=True)

    def update_book(self, book_id: str, updates: dict):
        idx = self.books_df.index[self.books_df["book_id"] == book_id]
        if len(idx) == 0:
            return False
        for k, v in updates.items():
            self.books_df.loc[idx, k] = v
        return True

    def set_book_availability(self, book_id: str, available: str):
        self.books_df.loc[self.books_df["book_id"] == book_id, "available"] = available

    
    def get_memberships(self):
        return self.memberships_df

    def add_membership(self, row: dict):
        self.memberships_df = pd.concat([self.memberships_df, pd.DataFrame([row])], ignore_index=True)

    def update_membership(self, membership_no: str, updates: dict):
        idx = self.memberships_df.index[self.memberships_df["membership_no"] == membership_no]
        if len(idx) == 0:
            return False
        for k, v in updates.items():
            self.memberships_df.loc[idx, k] = v
        return True

    
    def get_active_issues(self):
        return self.issues_df

    def create_issue(self, row: dict):
        self.issues_df = pd.concat([self.issues_df, pd.DataFrame([row])], ignore_index=True)

    def mark_returned(self, issue_id: str, fine_amount: int):
        idx = self.issues_df.index[self.issues_df["issue_id"] == issue_id]
        if len(idx) == 0:
            return False
        self.issues_df.loc[idx, "returned"] = "Yes"
        self.issues_df.loc[idx, "fine"] = fine_amount
        return True

    
    def add_fine_payment(self, row: dict):
        self.fines_df = pd.concat([self.fines_df, pd.DataFrame([row])], ignore_index=True)

    def total_fines_collected(self):
        if self.fines_df.empty:
            return 0
        return int(self.fines_df["amount"].sum())
