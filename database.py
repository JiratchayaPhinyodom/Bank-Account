import json


class BankDB:
    def __init__(self, name):
        """Create name in __init__."""
        self.name = name

    def insert(self, bank_account):
        """
        Build JSON string name new_data.I use try to command detect errors.
        Then I used try to open accounts.json , reading data
        and convert JSON string to be a python dictionary(dict) using json.load().
        If an error occurs I used except FileNotFoundError with open accounts.json to save the data and
        used 'w' which is the file writing mode.
        And using json.dump() is a method used for converting a Python Object to a JSON (stored as a file).
        The json.dump() method requires two arguments, initially a Python Object, that is new_data and data_file
        and I add one argument that we can help keep the json file organized and easy to read by using indent
        and inserting the value is 4.
        What to do only if there are no errors in the try block that will get data update a new_data
        and again used json.dump() to converting Python Objects to JSON Objects (store data in .json files).
        """
        new_data = {
            bank_account.number: {
                "name": bank_account.name,
                "balance": bank_account.balance
            }
        }
        try:
            with open("accounts.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("accounts.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("accounts.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    def search(self, account_number):
        """
        This function is used to find information of account number.
        First try to find name that I use data[account_number]["name"] and try to find number of balance that I used
        data[account_number]["balance"] this order used the same as order dictionary in python.
        Then If there are no errors in the try block that will except KeyError and print No data for account number.
        """
        try:
            with open("accounts.json", "r") as data_file:
                data = json.load(data_file)
            print(f'Name={data[account_number]["name"]}, Balance={data[account_number]["balance"]}')
        except KeyError:
            print(f'No data for account number: {account_number}')

    def delete(self, account_number):
        """
        This function is used to delete information of account number.
        First try to delete the account number that will use del data[account_number].
        Then If there are no errors in the try block that will except KeyError and print No data for account number
        """
        try:
            with open("accounts.json", "r") as data_file:
                data = json.load(data_file)
            del data[account_number]
            print(f'DELETE account {account_number}')
            data.update(data)
            with open("accounts.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except KeyError:
            print(f'No data for account number: {account_number}')

    def record_transaction(self, account, amount):
        """
        This function is used to count account balance with amount and insert the data to the account.py.
        """
        account.balance = account.balance + amount
        self.insert(account)

    def __repr__(self):
        """
        The object representation can be changed by implementing the __repr__ method,which is required to a string.
        """
        return f'BankDB(name="{self.name}")'
