#Test cases for Bank Application

import unittest
from bank_app import BankAccount, BankApp

class Testbank_app(unittest.TestCase):
	def test_that_bank_app_exists(self):
		self.account = BankAccount()
		self.app = BankApp('John', '9088776655', 'drag0nball$', 55000.0)
		self.app.accounts['9088776655'] = self.account

	def test_that_deposit_amount_function_is_valid(self):
		result = self.balance.deposit_money(5000.0)
		self.assertEqual(self.account.balance, 60000.0)
		self.assertEqual(result, "Deposited $5000.00. New balance: $60000.00")
