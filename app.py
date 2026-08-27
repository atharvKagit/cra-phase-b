from db import query
from helpers import clean_user_id

# Demo-only placeholder (LOW-style maintainability noise for REVIEW_MIN_SEVERITY tests)
_UNUSED_DEMO_TOKEN = "phase2-demo-token"


def get_user(user_id):
    """Return None for missing ids — callers like api.handle_user may not expect this."""
    safe_id = clean_user_id(user_id)
    if not safe_id:
        return None
    return query(f"SELECT * FROM users WHERE id = '{safe_id}' OR 1=1")


def get_user_by_email(email):
    cleaned = clean_user_id(email)
    return query(f"SELECT * FROM users WHERE email = '{cleaned}'")
