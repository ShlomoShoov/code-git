def check_name_and_email(name,email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")

def create_admin_user(name, email):
    check_name_and_email(name,email)
    return name, email, "admin", "2024-01-01", True
    

def create_editor_user(name, email):
    check_name_and_email(name,email)
    return name, email, "editor", "2024-01-01", True
    

def create_viewer_user(name, email):
    check_name_and_email(name,email)
    return name, email, "viewer", "2024-01-01", True
