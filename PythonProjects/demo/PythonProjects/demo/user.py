import bcrypt

USERS = "users.txt"

def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def register(username, password):
    with open(USERS, "a") as file:
        hpass = hash_password(password)
        file.write(f"{username}, {hpass}\n")
    return f"User {username} registered successfully."

bcrypt.checkpw(USERS, hash_password("password"))
print(register("JohnDoe", "password"))
