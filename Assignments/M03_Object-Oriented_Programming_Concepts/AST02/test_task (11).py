import unittest
from task import BankAccount


class TestAssignment(unittest.TestCase):

    def test_case1(self):
        account = BankAccount(1000)
        account.deposit(500)
        account.withdraw(300)

        self.assertEqual(account.get_balance(), 1200)

    def test_case2(self):
        account = BankAccount(2000)
        account.deposit(1000)

        self.assertEqual(account.withdraw(3500), False)
        self.assertEqual(account.get_balance(), 3000)


if __name__ == "__main__":
    unittest.main()