import json
import os
from datetime import datetime

FILE_PATH = "users.json"


def load_data():
    """Return JSON data as a Python dict."""
    if not os.path.exists(FILE_PATH):
        return {"users": []}

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    """Write Python dict to JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


# def add_user(username, email):
#     data = load_data()

#     new_user = {
#         "username": username,
#         "email": email
#     }

#     data["users"].append(new_user)
#     save_data(data)
#     return new_user


# def get_all_users():
#     data = load_data()
#     return data["users"]


# def delete_user(username):
#     data = load_data()
#     original_count = len(data["users"])

#     data["users"] = [
#         user for user in data["users"]
#         if user["username"] != username
#     ]

#     if len(data["users"]) == original_count:
#         return False  # user not found

#     save_data(data)
#     return True
