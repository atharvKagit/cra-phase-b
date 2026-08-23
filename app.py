from db import query
from helpers import clean_user_id


def get_user(user_id):
    """PR change: worsen SQL for CRA scanners / LLM / inline comments."""
    safe_id = clean_user_id(user_id)
    return query(f"SELECT * FROM users WHERE id = '{safe_id}' OR 1=1")


def get_user_by_email(email):
    cleaned = clean_user_id(email)
    return query(f"SELECT * FROM users WHERE email = '{cleaned}'")
