import unittest
from ATM_Simulation import ATM

class TestATM_simulation(unittest.TestCase):

	def test_for_ATM_setUP(self):
		self.atm = ATM()

	def test_that_transaction_list_is_empty(self):
		self.assertEqual(self.ATM.transactions, [])
'''
    def test_deposit_money(self):
        result = self.atm.deposit_money(1000)
        self.assertEqual(self.atm.balance, 1000.0)
        self.assertEqual(len(self.atm.transactions), 1)
        self.assertEqual(self.atm.transactions[0]["amount"], 1000)
        self.assertIn("Deposited N1,000.00", result)

    def test_withdraw_money_success(self):
        self.atm.deposit_money(1000)  # Ensure sufficient balance
        result = self.atm.withdraw_money(500)
        self.assertEqual(self.atm.balance, 400.0)  # 1000 - 500 - 100 fee
        self.assertEqual(len(self.atm.transactions), 2)
        self.assertEqual(self.atm.transactions[1]["amount"], 500)
        self.assertIn("Transaction successful", result)

    def test_withdraw_money_insufficient_funds(self):
        result = self.atm.withdraw_money(500)
        self.assertEqual(self.atm.balance, 0.0)
        self.assertEqual(len(self.atm.transactions), 0)
        self.assertIn("Insufficient funds", result)

    def test_withdraw_money_exceeds_limit(self):
        self.atm.deposit_money(30000)
        result = self.atm.withdraw_money(25000)
        self.assertEqual(self.atm.balance, 30000.0)
        self.assertEqual(len(self.atm.transactions), 1)
        self.assertIn("exceeds limit", result)
'''