import unittest
from employees_payroll import Semicolon_payroll

class Testemployees_payroll(unittest.TestCase):

	def test_SetUp(self):
		semicolon_payroll = Semicolon_payroll()

	def test_that_add_employee_function_is_valid(self):
		dispalyPayroll = Semicolon_payroll("Ada", "5", "9.75")
		self.assertEqual(dispalyPayroll.name, "Ada")
		self.assertEqual(dispalyPayroll.hours_worked, "5")
		self.assertEqual(dispalyPayroll.pay_rate, "9.75")