import unittest
from account import *


class TestFormula(unittest.TestCase):

    def setUp(self):
        self.acc1 = Account("john")
        self.acc2 = Account('jane')
        self.acc3 = Account(4)

    def test_init(self):
        self.assertEqual(self.acc1.get_name(), "john")
        self.assertEqual(self.acc2.get_name(), "jane")
        self.assertEqual(self.acc3.get_name(), 4)
        self.assertEqual(self.acc1.get_balance(), 0)
        self.assertEqual(self.acc2.get_balance(), 0)
        self.assertEqual(self.acc3.get_balance(), 0)
        self.acc1.deposit(10)
        self.acc2.deposit(14)
        self.acc3.deposit(5)
        self.assertEqual(self.acc1.get_balance(), 10)
        self.assertEqual(self.acc2.get_balance(), 14)
        self.assertEqual(self.acc3.get_balance(), 5)
        self.acc1.withdraw(5)
        self.acc2.withdraw(4)
        self.acc3.withdraw(3)
        self.assertEqual(self.acc1.get_balance(), 5)
        self.assertEqual(self.acc2.get_balance(), 10)
        self.assertEqual(self.acc3.get_balance(), 2)


    def test_deposit(self):
        self.assertEqual(self.acc1.deposit(4), True)
        self.assertEqual(self.acc1.deposit(-4), False)
        with self.assertRaises(ValueError):
            self.acc1.deposit("hhh")
            self.acc2.deposit("ten")
            self.acc3.deposit("jane")

    def test_withdraw(self):
        self.acc1.deposit(10)
        self.acc2.deposit(10)
        self.acc3.deposit(10)
        self.assertEqual(self.acc1.withdraw(4), True)
        self.assertEqual(self.acc1.withdraw(-4), False)
        self.assertEqual(self.acc2.withdraw(10), True)
        self.assertEqual(self.acc2.withdraw(-4), False)
        self.assertEqual(self.acc3.withdraw(11), False)
        self.assertEqual(self.acc3.withdraw(-4), False)
        with self.assertRaises(ValueError):
            self.acc1.withdraw("hhh")
            self.acc2.withdraw("ten")
            self.acc3.withdraw("jane")



if __name__ == '__main__':
    unittest.main()
