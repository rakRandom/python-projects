def create_account(create_user,
                   get_data):
    print("\n===== Creating an account =====\n")

    user_list = get_users(get_data, only_return=True)
    username: str = input("Enter a username.\n: ")
    while username in user_list:
        print("This username is already taken.")
        username = input("Enter a username.\n: ")

    while True:
        password: str = input("Enter a password.\n: ")
        if len(password) > 32:
            print("Your password cannot have more than 32 characters.")
        elif len(password) == 0:
            print("Your password cannot be empty.")
        else:
            break

    create_user(username, password)
    print("Account created successfully!")
    input("...")
    return username


def delete_account(username: str,
                   delete_user):
    print("\n===== Delete Account =====\n")
    if input("Are you sure? \"Yes\" to continue.\n: ").lower() != "yes":
        input("...")
        return False

    confirm_username: str = input("Enter your username to continue.\n: ")
    if confirm_username != username:
        input("...")
        return False

    delete_user(username)
    print("User deleted.")
    input("...")
    return True


def change_password(username: str,
                    get_data,
                    set_data):
    print("\n===== Change Password =====\n")
    while True:
        new_password: str = input("Enter your new password.\n: ")
        if new_password == get_data()[username]["password"]:
            print("Your new password cannot be the same as your old one.")
        elif len(new_password) > 32:
            print("Your new password cannot have more than 32 characters.")
        elif len(new_password) == 0:
            print("Password has not been changed.")
            return False
        else:
            break

    set_data(username, "password", new_password)
    print("Password setted successfully!")
    input("...")
    return True


def get_users(get_data,
              *,
              only_return=False):
    users = tuple(get_data().keys())
    if only_return is True:
        return users

    print("\nTable of users:")
    for user in users:
        print(f"- {user}")
    input("...")


def login_authentication(get_data):
    print("\n===== Login =====\n")

    username: str = input("Enter your username.\n: ")
    if username not in get_users(get_data, only_return=True):
        print("This username does not exist.")
        input("...")
        return None

    password: str = input("Enter your password.\n: ")
    if password != get_data()[username]["password"]:
        print("Incorrect password.")
        input("...")
        return None

    print("Login successfully!")
    input("...")
    return username
