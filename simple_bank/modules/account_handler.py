def create_account(create_user,
                   get_data
                   ) -> str | None:
    print("\n===== Creating an account =====\n")

    # Getting the username and checking if it is in the user list
    user_list = get_users(get_data, only_return=True)
    while True:
        username: str = input("Enter a username.\n: ")
        if len(username) > 64:
            print("Your username cannot have more than 64 characters.")
        elif len(username) == 0:
            print("Your username cannot be empty.")
        elif username in user_list:
            print("This username is already taken.")
        else:
            break

    # Getting the password
    while True:
        password: str = input("Enter a password.\n: ")
        if len(password) > 64:
            print("Your password cannot have more than 64 characters.")
        elif len(password) == 0:
            print("Your password cannot be empty.")
        else:
            break

    # Creating the user
    if create_user(username, password) is True:
        print("Account created successfully!")
        input("...")
        return username
    else:
        print("An error occurred. The account has not been created.")
        input("...")
        return None


def delete_account(username: str,
                   delete_user
                   ) -> bool:
    print("\n===== Delete Account =====\n")

    # Check 1
    if input("Are you sure? \"Yes\" to continue.\n: ").lower() != "yes":
        input("...")
        return False

    # Check 2
    confirm_username: str = input("Enter your username to continue.\n: ")
    if confirm_username != username:
        input("...")
        return False

    # Deleting the selected user
    if delete_user(username) is True:
        print("User deleted.")
        input("...")
        return True
    else:
        print("An error occurred. The user has not been deleted.")
        input("...")
        return False


def change_password(username: str,
                    get_data,
                    set_data
                    ) -> bool:
    print("\n===== Change Password =====\n")

    # Getting the new password
    while True:
        new_password: str = input("Enter your new password.\n: ")

        if new_password == get_data()[username]["password"]:
            print("Your new password cannot be the same as your old one.")
        elif len(new_password) > 64:
            print("Your new password cannot have more than 64 characters.")
        elif len(new_password) == 0:
            print("Password has not been changed.")
            return False
        else:
            break

    # Changing the password
    if set_data(username, "password", new_password) is True:
        print("Password setted successfully!")
        input("...")
        return True
    else:
        print("An error occurred. The password has not been changed.")
        input("...")
        return False


def login_authentication(get_data) -> str | None:
    print("\n===== Login =====\n")

    # Getting the username and checking if it is in the users list
    username: str = input("Enter your username.\n: ")
    if username not in get_users(get_data, only_return=True):
        print("This username does not exist.")
        input("...")
        return None

    # Getting the username and checking if it is correct
    password: str = input("Enter your password.\n: ")
    if password != get_data()[username]["password"]:
        print("Incorrect password.")
        input("...")
        return None

    # Otherwise, the login will be successfull
    print("Login successfully!")
    input("...")
    return username


def get_users(get_data,
              *,
              only_return=False
              ) -> tuple:
    users = tuple(get_data().keys())
    if only_return is True:  # With this condition it became possible to use this function without printing
        return users

    print("\nTable of users:")
    for user in users:
        print(f"- {user}")

    input("...")
