# import unittest
import pytest
from account import *


class Test:
    def setup_method(self):
        self.acc1 = Account("john")
        self.acc2 = Account('jane')
        self.acc3 = Account(4)

    def test_init(self):
        assert self.acc1.get_name() == "john"
        assert self.acc2.get_name() == "jane"
        assert self.acc3.get_name() == 4
        assert self.acc1.get_balance() == 0
        assert self.acc2.get_balance() == 0
        assert self.acc3.get_balance() == 0
        self.acc1.deposit(10)
        self.acc2.deposit(14)
        self.acc3.deposit(5)
        assert self.acc1.get_balance() == 10
        assert self.acc2.get_balance() == 14
        assert self.acc3.get_balance() == 5
        self.acc1.deposit(1.5)
        self.acc2.deposit(1.4)
        self.acc3.deposit(.5)
        assert self.acc1.get_balance() == 11.5
        assert self.acc2.get_balance() == 15.4
        assert self.acc3.get_balance() == 5.5
        self.acc1.withdraw(5)
        self.acc2.withdraw(4)
        self.acc3.withdraw(3)
        assert self.acc1.get_balance() == 6.5
        assert self.acc2.get_balance() == 11.4
        assert self.acc3.get_balance() == 2.5

    def test_deposit(self):
        assert self.acc1.deposit(4) is True
        assert self.acc1.deposit(-4) is False
        with pytest.raises(ValueError):
            self.acc1.deposit("hhh")
            self.acc2.deposit("ten")
            self.acc3.deposit("jane")

    def test_withdraw(self):
        self.acc1.deposit(10)
        self.acc2.deposit(10)
        self.acc3.deposit(10)
        assert self.acc1.withdraw(4) is True
        assert self.acc1.withdraw(-4) is False
        assert self.acc2.withdraw(10) is True
        assert self.acc2.withdraw(-4) is False
        assert self.acc3.withdraw(11) is False
        assert self.acc3.withdraw(-4) is False
        with pytest.raises(ValueError):
            self.acc1.withdraw("hhh")
            self.acc2.withdraw("ten")
            self.acc3.withdraw("jane")

# if __name__ == '__main__':
#     unittest.main()
