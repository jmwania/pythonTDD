import unittest
from bank_account import BankAccount, Subclass

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.my_account = BankAccount()
    
    def test_Balance(self):
        self.assertEqual(self.my_account.balance, 5000, msg='Not able to retrieveaccount balance')
        
    def test_deposit(self):
        self.my_account.deposit(3000)
        self.assertEqual(self.my_account.balance, 8000, msg='Inncorect deposit')
        
    def test_subclass(self):
        self.assertTrue(issubclass(Subclass, BankAccount), msg='Not a subclass')

if __name__ == "__main__":
    unittest.main()