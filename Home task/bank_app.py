#Bank Application

class BankAccount:
	def create_account():
		self.name = name
		self.account_number = account_number
		self.password = password
		self.balance = balance

	def deposit_money(self, amount):
		if amount > 0:
			self.balance += amount
			return f'Deposited ${amount:.2f}. New balance: ${self.balance:.2f}'
		return 'Invalid deposit amount'

class BankApp:
	def __init__(self, name, account_number, password, balance = 0.0):
		self.accounts = {}
		self.current_user = None