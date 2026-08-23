from app import get_user


def handle_user(user_id):
    # Lives on main so impact analysis can find this caller when PRs edit app.py
    return get_user(user_id)
