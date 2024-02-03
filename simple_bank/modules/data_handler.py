import json

DATA_PATH = "data/accounts.json"


def get_data() -> dict:
    with open(DATA_PATH, "r") as file:
        data = json.loads(file.read())
    if data:
        return data
    else:
        return {}


def set_data(username: str,
             attr: str,
             new_val):
    data = get_data()
    if username not in data.keys():
        print("User does not exist.")
        return

    data[username][attr] = new_val

    with open(DATA_PATH, "w") as file:
        file.write(json.dumps(data, indent=4))


def create_user(username: str,
                password: str):
    data = get_data()
    if username in data.keys():
        print("This username is already taken.")
        return

    user = {
        username: {
            "password": password,
            "money": 0
        }
    }
    data.update(user)

    with open(DATA_PATH, "w") as file:
        file.write(json.dumps(data, indent=4))


def delete_user(username: str):
    data = get_data()
    if username not in data.keys():
        print("User does not exist.")
        return

    del data[username]

    with open(DATA_PATH, "w") as file:
        file.write(json.dumps(data, indent=4))


def update_money(username: str,
                 change: int):
    data = get_data()
    if username not in data.keys():
        print("User does not exist.")
        return

    data[username]["money"] += change

    with open(DATA_PATH, "w") as file:
        file.write(json.dumps(data, indent=4))
