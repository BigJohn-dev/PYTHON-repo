import unittest
from payroll import payroll

class Testpayroll(unittest.TestCase):

	def test_that_functions_exist(self):
		self.assertTrue(callable(payroll.gross_pay))
		self.assertTrue(callable(payroll.federalTax))
		self.assertTrue(callable(payroll.stateTax))

	def test_gross_pay(self):
		self.assertEqual(payroll.gross_pay(25, 40), 1000)
		self.assertEqual(payroll.gross_pay(15.50, 10), 155.0)

	def test_federal_tax(self):
		self.assertEqual(payroll.federalTax(25), 5)
		self.assertEqual(payroll.federalTax(15.50), 3.1)

	def test_state_tax(self):
		self.assertEqual(payroll.stateTax(25), 2.25)
		self.assertEqual(payroll.stateTax(15.50), 1.395)