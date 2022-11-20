# import unittest
import pytest
from account import *


class Test:
    def setup_method(self):
        self.acc1 = Account("john")
        self.acc2 = Account('jane')
        self.acc3 = Account(4)

    def teardown_method(self):
        del self.acc1
        del self.acc2
        del self.acc3
    def test_init(self):
        assert self.acc1.get_name() == "john"
        assert self.acc2.get_name() == "jane"
        assert self.acc3.get_name() == 4.0
        assert self.acc1.get_balance() == pytest.approx(0.0, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(0.0, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(0.0, abs=0.001)
        self.acc1.deposit(10)
        self.acc2.deposit(14)
        self.acc3.deposit(5)
        assert self.acc1.get_balance() == pytest.approx(10.0, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(14.0, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(5.0, abs=0.001)
        self.acc1.deposit(1.5)
        self.acc2.deposit(1.4)
        self.acc3.deposit(.5)
        assert self.acc1.get_balance() == pytest.approx(11.5, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(15.4, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(5.5, abs=0.001)
        self.acc1.withdraw(5)
        self.acc2.withdraw(4)
        self.acc3.withdraw(3)
        assert self.acc1.get_balance() == pytest.approx(6.5, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(11.4, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(2.5, abs=0.001)

    def test_deposit(self):
        assert self.acc1.deposit(4) is True
        assert self.acc1.deposit(-4) is False
        assert self.acc1.deposit(6.5) is True
        assert self.acc2.deposit(15.4) is True
        assert self.acc3.deposit(5.5) is True
        assert self.acc1.deposit(0) is False
        assert self.acc2.deposit(0) is False
        assert self.acc3.deposit(0) is False
        assert self.acc1.get_balance() == pytest.approx(10.5, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(15.4, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(5.5, abs=0.001)
        with pytest.raises(ValueError):
            self.acc1.deposit("hhh")
            self.acc2.deposit("ten")
            self.acc3.deposit("jane")

    def test_withdraw(self):
        self.acc1.deposit(100)
        self.acc2.deposit(100)
        self.acc3.deposit(100)
        assert self.acc1.withdraw(4) is True
        assert self.acc1.withdraw(-4) is False
        assert self.acc2.withdraw(10) is True
        assert self.acc2.withdraw(-4) is False
        assert self.acc3.withdraw(110) is False
        assert self.acc3.withdraw(-4) is False
        assert self.acc1.withdraw(0) is False
        assert self.acc2.withdraw(0) is False
        assert self.acc3.withdraw(0) is False
        assert self.acc1.get_balance() == pytest.approx(96.0, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(90.0, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(100.0, abs=0.001)
        assert self.acc1.withdraw(11.5) is True
        assert self.acc2.withdraw(2.4) is True
        assert self.acc3.withdraw(3.33) is True
        assert self.acc1.get_balance() == pytest.approx(84.5, abs=0.001)
        assert self.acc2.get_balance() == pytest.approx(87.6, abs=0.001)
        assert self.acc3.get_balance() == pytest.approx(96.67, abs=0.001)
        with pytest.raises(ValueError):
            self.acc1.withdraw("hhh")
            self.acc2.withdraw("ten")
            self.acc3.withdraw("jane")

# if __name__ == '__main__':
#     unittest.main()
