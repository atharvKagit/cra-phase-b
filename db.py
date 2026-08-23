def query(sql: str):
    """Fake DB executor for demos — does not talk to a real database."""
    return {"sql": sql, "rows": []}
