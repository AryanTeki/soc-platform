def validate_username(username):
    return isinstance(username, str) and len(username) > 0

def validate_password(password):
    return isinstance(password, str) and len(password) >= 6

# Additional utility functions can be added here.
