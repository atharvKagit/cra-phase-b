def clean_user_id(value):
    """Very weak sanitizer on purpose — still unsafe for CRA demos."""
    return str(value).replace(";", "")
