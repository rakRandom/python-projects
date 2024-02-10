import mysql.connector
from sys import exit as sysexit


class DataHandler:
    def __init__(self):
        self.host: str = "localhost"  # The host of your database | Default: localhost
        self.user: str = "root"  # Your username | Default: root
        self.password: str = "1234"  # Your password | Default: 1234
        self.database: str = "banco"  # The MySQL scheme name | Default: banco
        self.table: str = "users"  # The MySQL users table | Default: users

        # Connecting to the DB
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error: Unable to connect to the database. Check if MySQL is downloaded and if {self.database} exists.")
            print(f"Exception: {e}")
            sysexit(1)

        # Checking if the table exists
        self.cursor.execute('SHOW TABLES')
        table_list = [item[0] for item in self.cursor.fetchall()]

        # If it does not exist, create
        try:
            if self.table not in table_list:
                self.cursor.execute(f"""CREATE TABLE {self.database}.{self.table} (
                                        `id` INT NOT NULL AUTO_INCREMENT,
                                        `username` VARCHAR(64) NOT NULL,
                                        `password` VARCHAR(64) NOT NULL,
                                        `money` DECIMAL(65,30) NULL,
                                        PRIMARY KEY (`id`),
                                        UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)""")

                self.connection.commit()
        except Exception as e:
            print(f"Error: Unable to create users table. Check if database name and table name are written correctly.")
            print(f"Exception: {e}")
            sysexit(1)

    def get_data(self) -> dict:
        self.cursor.execute(f'SELECT * FROM {self.table}')
        data = {
            val[1]: {
                "password": val[2],
                "money": float(val[3])
            } for val in self.cursor.fetchall()
        }

        if data:
            return data
        else:
            return {}

    def set_data(self,
                 username: str,
                 attr: str,
                 new_val) -> bool:
        data: dict = self.get_data()
        if username not in data.keys():
            print("User does not exist.")
            return False

        try:
            self.cursor.execute(f'UPDATE {self.table} SET {attr} = "{new_val}" WHERE username = "{username}"')
        except mysql.connector.InterfaceError as e:
            print(f"Error: {e}")
        except mysql.connector.ProgrammingError as e:
            print(f"Error: {e}")
        else:
            self.connection.commit()
            return True
        return False

    def create_user(self,
                    username: str,
                    password: str) -> bool:
        data: dict = self.get_data()
        if username in data.keys():
            print("This username is already taken.")
            return False

        try:
            self.cursor.execute(f'INSERT INTO {self.table} (username, password, money) VALUES ("{username}", "{password}", 0)')
        except mysql.connector.InterfaceError as e:
            print(f"Error: {e}")
        except mysql.connector.ProgrammingError as e:
            print(f"Error: {e}")
        else:
            self.connection.commit()
            return True
        return False

    def delete_user(self,
                    username: str) -> bool:
        data: dict = self.get_data()
        if username not in data.keys():
            print("User does not exist.")
            return False

        try:
            self.cursor.execute(f'DELETE FROM {self.table} WHERE username = "{username}"')
        except mysql.connector.InterfaceError as e:
            print(f"Error: {e}")
        except mysql.connector.ProgrammingError as e:
            print(f"Error: {e}")
        else:
            self.connection.commit()
            return True
        return False

    def update_money(self,
                     username: str,
                     change: int) -> bool:
        data: dict = self.get_data()
        if username not in data.keys():
            print("User does not exist.")
            return False

        try:
            self.cursor.execute(f'UPDATE {self.table} SET money = {data[username]["money"] + change} WHERE username = "{username}"')
        except mysql.connector.InterfaceError as e:
            print(f"Error: {e}")
        except mysql.connector.ProgrammingError as e:
            print(f"Error: {e}")
        else:
            self.connection.commit()
            return True
        return False

    def close(self) -> None:  # Method to close the connection with the database
        print("\nClosing...")
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print(f"Error: {e}")
        else:
            print("Closed.")
