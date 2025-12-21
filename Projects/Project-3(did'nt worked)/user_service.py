from storage import load_data, save_data
from datetime import datetime


def _find_user_index(username, users):
    for index, user in enumerate(users):
        if user["username"] == username:
            return index
    return None


def add_user(username, email):
    data = load_data()
    users = data["users"]

    # Validation
    if len(username) < 3:
        return "Username too short."

    if "@" not in email:
        return "Invalid email."

    # Email must be unique
    for user in users:
        if user["email"] == email:
            return "Email already exists."

    new_user = {
        "username": username,
        "email": email,
        "created_at": datetime.now().isoformat(),
        "updated_at": None
    }

    users.append(new_user)
    save_data(data)
    return new_user


def get_all_users():
    data = load_data()
    return data["users"]


def update_user(username, new_email):
    data = load_data()
    users = data["users"]

    idx = _find_user_index(username, users)
    if idx is None:
        return "User not found."

    if "@" not in new_email:
        return "Invalid email."

    users[idx]["email"] = new_email
    users[idx]["updated_at"] = datetime.now().isoformat()

    save_data(data)
    return users[idx]


def delete_user(username):
    data = load_data()
    users = data["users"]

    idx = _find_user_index(username, users)
    if idx is None:
        return "User not found."

    deleted_user = users.pop(idx)
    save_data(data)
    return deleted_user
