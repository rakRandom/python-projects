def withdraw_money(username: str,
                   current_money: float,
                   update_money):
    print("\n===== Withdrawing =====\n")
    try:
        money_to_withdraw: float = float(input("How much money you want to withdraw?\n: R$").replace(",", "."))
    except ValueError:
        print("Error: Make sure you write the number correctly.")
        return

    if money_to_withdraw > current_money:
        print("You do not have enough money.")
        input("...")
        return
    update_money(username, -money_to_withdraw)
    print("Withdrawal made successfully!")
    input("...")


def deposit_money(username: str,
                  update_money):
    print("\n===== Depositing =====\n")
    try:
        money_to_deposit: float = float(input("How much money you want to deposit?\n: R$").replace(",", "."))
    except ValueError:
        print("Error: Make sure you write the number correctly.")
        return

    update_money(username, money_to_deposit)
    print("Deposit made successfully!")
    input("...")


def transfer_money(user_to_transfer: str,
                   current_money: float,
                   user_list: tuple,
                   update_money):
    print("\n===== Transferring =====\n")
    try:
        money_to_transfer: float = float(input("How much money you want to transfer?\n: R$").replace(",", "."))
    except ValueError:
        print("Error: Make sure you write the number correctly.")
        return

    if money_to_transfer > current_money:
        print("You do not have enough money.")
        input("...")
        return

    user_to_recive: str = input(f"Enter the name of the user who will receive R${money_to_transfer:.2f}.\n: ")
    if user_to_recive not in user_list:
        print("This user does not exist.")
        input("...")
        return

    update_money(user_to_transfer, -money_to_transfer)
    update_money(user_to_recive, money_to_transfer)
    print("Transaction made successfully!")
    input("...")
