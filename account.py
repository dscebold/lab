

class Account:

    def __init__(self, name):
        """
        This is the constructor method for the Account class
        takes in the account name to be assigned and sets balance to zero
        :param name: name of the Account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        """
        This method increases account_balance by adding amount
        :param amount: amount to be deposited into account
        :return: Returns true if deposit was successful, returns false if deposit was unsuccessful
        """
        if amount < 0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount):
        """
        This method decreases account_balance by subtracting amount
        :param amount: amount to be withdrawn from account
        :return: Returns true if withdraw was successful, returns false if withdraw was unsuccessful
        """
        if amount < 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self):
        """
        Gets the account_balance
        :return: Returns the account balance
        """
        return self.__account_balance

    def get_name(self):
        """
        Gets the account_name
        :return: Returns the account name
        """
        return self.__account_name
