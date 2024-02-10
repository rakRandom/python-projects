from modules.data_handler import DataHandler
from modules import cash_handler as cash_h
from modules import account_handler as account_h
from sys import exit
from time import sleep


def loading(times=1):
    sleep(0.5)
    for _ in range(times):
        print("\rLoading", end="")
        sleep(0.25)
        print(".", end="")
        sleep(0.25)
        print(".", end="")
        sleep(0.25)
        print(".", end="")
        sleep(0.25)
    print("\r ", end="")


def main(data_h: DataHandler):
    username: str | None = None
    user_selection: int

    print("========== Welcome to the PyBank! ==========")
    loading(2)
    while username is None:
        user_selection = int(input("\nWhat you want to do?\n[1] Login\n[2] Create Account\n[0] Exit\n: "))
        loading()
        match user_selection:
            case 1:  # Login
                username = account_h.login_authentication(data_h.get_data)
            case 2:  # Create account
                username = account_h.create_account(data_h.create_user, data_h.get_data)
            case _:  # Exit
                exit(0)

    print(f"\nHello, {username}!", end=" ")

    while True:
        print(f"\nYou have R${data_h.get_data()[username]["money"]:.2f}")
        user_selection = int(input("""
What you want to do?
[1] Withdraw
[2] Deposit
[3] Transfer
[4] Get Users List
[5] Change Password
[6] Delete Account
[0] Exit
: """))

        loading()
        match user_selection:
            case 1:  # Withdraw
                cash_h.withdraw_money(
                    username,
                    data_h.get_data()[username]["money"],
                    data_h.update_money
                )
            case 2:  # Deposit
                cash_h.deposit_money(
                    username,
                    data_h.update_money
                )
            case 3:  # Transfer
                cash_h.transfer_money(
                    username,
                    data_h.get_data()[username]["money"],
                    account_h.get_users(data_h.get_data, only_return=True),
                    data_h.update_money
                )
            case 4:  # Get users list
                account_h.get_users(data_h.get_data)
            case 5:  # Change password
                account_h.change_password(
                    username,
                    data_h.get_data,
                    data_h.set_data
                )
            case 6:  # Delete account
                if account_h.delete_account(username, data_h.delete_user) is True:
                    break
            case _:  # Exit
                exit(0)


if __name__ == '__main__':
    data_handler = DataHandler()

    try:
        while True:
            main(data_handler)
    finally:
        data_handler.close()
