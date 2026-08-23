from db import query
from helpers import clean_user_id


def get_user(user_id):
    """Baseline on main — still not production-safe, but no OR 1=1 yet."""
    safe_id = clean_user_id(user_id)
    return query(f"SELECT * FROM users WHERE id = '{safe_id}'")


def get_user_by_email(email):
    cleaned = clean_user_id(email)
    return query(f"SELECT * FROM users WHERE email = '{cleaned}'")
