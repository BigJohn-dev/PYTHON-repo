import unittest
from bank_app import Bank, BankAccount

class TestBankApp(unittest.TestCase):
	def test_that_get_bank_function_exists(self):
		self.bank = Bank()

	def test_account_can_be_created(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		self.assertEqual(account.name, "John Floss")
		self.assertEqual(account.account_number, "9090997988")
		self.assertEqual(account.password, "dragonballs")
		self.assertEqual(account.balance, 5000.0)

	def test_deposit_money_is_valid(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.deposit_money(1000.0)
		self.assertEqual(account.balance, 6000.0)
		self.assertEqual(result, "Deposited $1000.00. New balance: $6000.00")

	def test_withdraw_money_valid(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.withdraw_money(2000.0)
		self.assertEqual(account.balance, 3000.0)
		self.assertEqual(result, "Withdrew $2000.00. New balance: $3000.00")

	def test_deposit_money_valid(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.deposit_money(1000.0)
		self.assertEqual(account.balance, 6000.0)
		self.assertEqual(result, "Deposited $1000.00. New balance: $6000.00")

	def test_deposit_money_is_not_negative(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 0.0)
		result = account.deposit_money(-1000.0)
		self.assertEqual(account.balance, 0.0)
		self.assertEqual(result, "Invalid deposit amount")
		result = account.deposit_money(0.0)
		self.assertEqual(account.balance, 0.0)
		self.assertEqual(result, "Invalid deposit amount")
