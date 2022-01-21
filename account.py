class BankAccount:
    def __init__(self, number, name, balance, db):
        """Create number, name, balance, db(database) and db.insert(database insert) in __init__."""
        self.number = number
        self.name = name
        self.balance = balance
        self.db = db
        db.insert(self)

    """
    @property decorator wraps getter/setter methods to create a property, 
    which can be directly accessed as if it was a public attribute
    """
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        """This setter allow only string account number must be a string"""
        if not isinstance(number, str):
            raise TypeError("account number must be a string")
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """This setter allow only string account name must be a string"""
        if not isinstance(name, str):
            raise TypeError("account name must be a string")
        self.__name = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        """This setter allow only int or float balance must be a number
        and make a condition if balance less than or equal 0 raise ValueError balance must be greater than zero."""

        if not isinstance(balance, (int, float)):
            raise TypeError("balance must be a number")
        if balance <= 0:
            raise ValueError("balance must be greater than zero")
        self.__balance = balance

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    def deposit(self, amount):
        """
        This function will deposit the money in the bank account.
        First I use self.db.record_transaction(self, amount) order to use record_transaction function in database.py
        that will count account balance with amount and insert the data to the account.py.
        Last the function will show UPDATE account {number of account} balance = {balance of account}
        """
        # add your implementation
        self.db.record_transaction(self, amount)
        print(f'UPDATE account {self.number} balance = {self.balance}')

    def withdraw(self, amount):
        """
        This function will withdraw the money in the bank account.
        First If amount less than balance I use self.db.record_transaction(self, amount) order
        to use record_transaction function in database.py that will count account balance with amount
        and insert the data to the account.py.
        Then the function will show UPDATE account {number of account} balance = {balance of account}.
        If amount > balance the program will show Not enough money.
        """
        if amount < self.balance:
            self.db.record_transaction(self, -1 * amount)
            print(f'UPDATE account {self.number} balance = {self.balance}')
        else:
            print("Not enough money")

    def transfer(self, amount, to_account):
        """
        This function will transfer money to another account.
        First make a condition if amount < balance that will withdraw the money in this account
        and deposit money to another account.
        """
        if amount < self.balance:
            self.withdraw(amount)
            to_account.deposit(amount)
        else:
            print("Not enough money")

    def __repr__(self):
        """
        The object representation can be changed by implementing the __repr__ method,which is required to a string.
        """
        return f'Account(number="{self.number}", name="{self.name}", balance={self.balance}, db="{self.db.name}")'



