

class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount < 0:
            return False
        self.__account_balance += amount
        return True