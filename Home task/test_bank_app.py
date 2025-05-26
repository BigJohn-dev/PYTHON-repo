import unittest
from bank_app import Bank, BankAccount

class TestBankApp(unittest.TestCase):
	def test_for_bank_setUP(self):
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

	def test_deposit_money_is_not_negative(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 0.0)
		result = account.deposit_money(-1000.0)
		self.assertEqual(account.balance, 0.0)
		self.assertEqual(result, "Invalid deposit amount")

	def test_withdraw_money_valid(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.withdraw_money(2000.0)
		self.assertEqual(account.balance, 3000.0)
		self.assertEqual(result, "Withdrew $2000.00. New balance: $3000.00")

	def test_withdraw_money_is_not_beyond_balance(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.withdraw_money(7000.0)
		self.assertEqual(account.balance, 5000.0)
		self.assertEqual(result, "Invalid withdrawal amount or insufficient funds")

	def test_withdraw_money_is_not_negative(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.withdraw_money(-1000.0)
		self.assertEqual(account.balance, 5000.0)
		self.assertEqual(result, "Invalid withdrawal amount or insufficient funds")

	def test_account_to_check_balance(self):
		account = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		result = account.check_balance()
		self.assertEqual(result, "Balance for John Floss: $5000.00")

	def test_transfer_is_valid(self):
		sender = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		recipient = BankAccount("Megow", "1122334455", "ninjago", 500.0)
		result = sender.transfer(1500.0, recipient)
		self.assertEqual(sender.balance, 3500.0)
		self.assertEqual(recipient.balance, 2000.0)
		self.assertEqual(result, "Transferred $1500.00 to Megow. Your new balance: $3500.00")

	def test_transfer_insufficient_funds(self):
		sender = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		recipient = BankAccount("Megow", "1122334455", "ninjago", 500.0)
		result = sender.transfer(5500.0, recipient)
		self.assertEqual(sender.balance, 5000.0)
		self.assertEqual(recipient.balance, 500.0)
		self.assertEqual(result, "Invalid transfer amount or insufficient funds")

	def test_transfer_negative_amount(self):
		sender = BankAccount("John Floss", "9090997988", "dragonballs", 5000.0)
		recipient = BankAccount("Megow", "1122334455", "ninjago", 500.0)
		result = sender.transfer(-1000.0, recipient)
		self.assertEqual(sender.balance, 5000.0)
		self.assertEqual(recipient.balance, 500.0)
		self.assertEqual(result, "Invalid transfer amount or insufficient funds")

	def test_recover_account(self):
		self.bank.create_account("John Floss", "9090997988", "dragonballs", 5000.0)
		result = self.bank.recover_account("John Floss", "9090997988", "newpassword")
		self.assertEqual(result, "Password updated for John Floss")
		account = self.bank.get_account("9090997988")
		self.assertEqual(account.password, "newpassword")