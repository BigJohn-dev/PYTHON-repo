import unittest
from ATM_simulation import ATM

class TestATM_simulation(unittest.TestCase):
	def test_for_ATM_setUP(self):
		self.atm = ATM()

	def test_deposit_money_is_valid(self):
		atm = ATM(5000.0)
		result = atm.deposit_money(1000.0)
		self.assertEqual(atm.balance, 6000.0)
		self.assertEqual(result, "Deposited N1,000.00. New balance: N6,000.00")

	def test_deposit_money_is_not_negative(self):
		atm = ATM(6000.0)
		result = atm.deposit_money(-1000.0)
		self.assertEqual(atm.balance, 6000.0)
		self.assertEqual(result, "Invalid deposit amount")

	def test_withdraw_money_valid(self):
		atm = ATM(5000.0)
		result = atm.withdraw_money(2000.0)
		self.assertEqual(atm.balance, 2900.0)
		self.assertEqual(result, f"\nTransaction successful \nWithdrawal amount: N2,000.00. \nWithdrawal fee: N 100. \nNew balance: N2,900.00.")

	def test_withdraw_money_is_not_beyond_balance(self):
		atm = ATM(5000.0)
		result = atm.withdraw_money(7000.0)
		self.assertEqual(atm.balance, 5000.0)
		self.assertEqual(result, "Invalid withdrawal amount or insufficient funds")

	def test_withdraw_money_is_not_beyond_limit(self):
		atm = ATM(50000.0)
		result = atm.withdraw_money(30000.0)
		self.assertEqual(atm.balance, 50000.0)
		self.assertEqual(result, "Exceeded withdrawal limit ")

	def test_withdraw_money_is_not_negative(self):
		atm = ATM(5000.0)
		result = atm.withdraw_money(-1000.0)
		self.assertEqual(atm.balance, 5000.0)
		self.assertEqual(result, "Invalid withdrawal amount or insufficient funds")

	def test_ATM_to_check_balance(self):
		atm = ATM(5000.0)
		result = atm.check_balance()
		self.assertEqual(result, "Balance: N5,000.00")
