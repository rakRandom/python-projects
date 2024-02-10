def withdraw_money(username: str,
                   current_money: float,
                   update_money
                   ) -> bool:
    print("\n===== Withdrawing =====\n")

    # Getting how much the user want to withdraw
    while True:
        try:
            money_to_withdraw: float = float(input("How much money you want to withdraw?\n: R$").replace(",", "."))
        except ValueError:
            print("Error: Make sure you write the number correctly.")
        else:
            break

    # Checking if the user has the money
    if money_to_withdraw > current_money:
        print("You do not have enough money.")
        input("...")
        return False

    # Withdrawing the money
    if update_money(username, -money_to_withdraw) is True:
        print("Withdrawal made successfully!")
        input("...")
        return True
    else:
        print("An error occurred. The withdrawal was not made.")
        input("...")
        return False


def deposit_money(username: str,
                  update_money
                  ) -> bool:
    print("\n===== Depositing =====\n")

    # Getting how much the user want to deposit
    while True:
        try:
            money_to_deposit: float = float(input("How much money you want to deposit?\n: R$").replace(",", "."))
        except ValueError:
            print("Error: Make sure you write the number correctly.")
        else:
            break

    # Depositing the money
    if update_money(username, money_to_deposit) is True:
        print("Deposit made successfully!")
        input("...")
        return True
    else:
        print("An error occurred. The deposit was not made.")
        input("...")
        return False


def transfer_money(user_to_transfer: str,
                   current_money: float,
                   user_list: tuple,
                   update_money
                   ) -> bool:
    print("\n===== Transferring =====\n")

    # Getting how much the user want to transfer
    try:
        money_to_transfer: float = float(input("How much money you want to transfer?\n: R$").replace(",", "."))
    except ValueError:
        print("Error: Make sure you write the number correctly.")
        return False

    # Checking if the user has the money
    if money_to_transfer > current_money:
        print("You do not have enough money.")
        input("...")
        return False

    # Getting the username of who will recive the money
    user_to_recive: str = input(f"Enter the name of the user who will receive R${money_to_transfer:.2f}.\n: ")

    # Checking if the user who will recive the money exists
    if user_to_recive not in user_list:
        print("This user does not exist.")
        input("...")
        return False

    # Transfering from one user to another
    if update_money(user_to_transfer, -money_to_transfer) is False:
        print("An error occurred. The transaction was not made.")
        input("...")
        return False
    if update_money(user_to_recive, money_to_transfer) is False:
        print("An error occurred. The transaction was not made.")
        update_money(user_to_transfer, money_to_transfer)
        input("...")
        return False

    print("Transaction made successfully!")
    input("...")
    return True
