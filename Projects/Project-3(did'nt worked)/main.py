from user_service import add_user, get_all_users, delete_user, update_user

def menu():
    print("\n--- USER MANAGEMENT SYSTEM ---")
    print("1. Add User")
    print("2. Show All Users")
    print("3. Update User Email")
    print("4. Delete User")
    print("5. Exit")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            response = add_user(username, email)
            print("Result:", response)

        elif choice == "2":
            for u in get_all_users():
                print(f"{u['username']} | {u['email']} | Created: {u['created_at']} | Updated: {u['updated_at']}")

        elif choice == "3":
            username = input("Username to update: ")
            new_email = input("New email: ")
            result = update_user(username, new_email)
            print("Result:", result)

        elif choice == "4":
            username = input("Username to delete: ")
            result = delete_user(username)
            print("Result:", result)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
