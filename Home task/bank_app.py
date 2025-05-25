# Creating a Banking application

class BankAccount:

	def __init__(self, name, account_number, password, balance = 0.0):
		self.name = name
		self.account_number = account_number
		self.password = password
		self.balance = balance

	def deposit_money(self, amount):
		if amount > 0:
			self.balance += amount
			return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
		else:
			return "Invalid deposit amount"

	def withdraw_money(self, amount):
		if amount > 0 and self.balance >= amount:
			self.balance -= amount
			return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
		else:
			return "Invalid withdrawal amount or insufficient funds"

	def check_balance(self):
		return  f"Balance for {self.name}: ${self.balance:.2f}"

	def transfer(self, amount, recipient):
		if 0 < amount <= self.balance:
			self.balance -= amount
			recipient.balance += amount
			return f"Transferred ${amount:.2f} to {recipient.name}. Your new balance: ${self.balance:.2f}"
		return "Invalid transfer amount or insufficient funds"


class Bank:
	
	def __init__(self):
		self.accounts = {}
		self.current_user = None

	def create_account(self, name, account_number, password, balance = 0.0):
		if account_number not in self.accounts:
			new_account = BankAccount(name, account_number, password, balance)
			self.accounts[account_number] = new_account
			return f"Account created for {name}"
		else:
			return f"Account {account_number} already exists"
	
	def log_in(self, account_number, password):
		if account_number in self.accounts and self.accounts[account_number].password == password:
			self.current_user = self.accounts[account_number]
			return f"Logged in as {self.current_user.name}"
		else:
			return "Account not found or incorrect password"

	def get_account(self, account_number):
		return self.accounts.get(account_number)
		
	def recover_account(self, name, account_number, new_password):
		account = self.get_account(account_number)
		if account and account.name == name:
			account.password = new_password
			return f"Password reset successfully for {name}"
		return "Account not found or name does not match"

def main():
	bank = Bank()
	while True:
		if not bank.current_user:
			menu = """
WELCOME TO PYTHON BANK

...select an option

1. Create Account
2. Login
3. Recover account
4. Exit
			"""
			print(menu)
			try:
				user_choice = int(input())

			except ValueError:
				print("Invalid input. Please enter a number.")
				continue

			if user_choice == 1:
				print("CREATE ACCOUNT")
				username = input("\nEnter username: ")
				account_number = input("Enter account number: ")
				password = input("Enter password: ")
				print(bank.create_account(username, account_number, password))

			elif user_choice == 2:
				print("LOGIN TO YOUR ACCOUNT")
				account_number = input("\nEnter account number: ")
				password = input("Enter password: ")
				print(bank.log_in(account_number, password))

			elif user_choice == 3:
				print("RECOVER ACCOUNT")
				username = input("\nEnter your username: ")
				account_number = input("Enter account number: ")
				new_password = input("Enter new password: ")
				print(bank.recover_account(username, account_number, new_password))
				

			elif user_choice == 4:
				print("...thank you for banking with us!")
				print("...PYTHON BANK")
				break

			else:
				print("Invalid option")
		
		else:
			print(f"\nWelcome, {bank.current_user.name}")
			print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Logout")
			choice = input("\nChoose an option: ")

			if choice == "1":
				print(bank.current_user.check_balance())

			elif choice == "2":
				try:
					amount = float(input("Enter deposit amount: "))
					print(bank.current_user.deposit_money(amount))
				except ValueError:
					print("Invalid amout. Please enter a number.")

			elif choice == "3":
				try:
					amount = float(input("Enter withdrawal amount: "))
					print(bank.current_user.withdraw_money(amount))
				except ValueError:
					print("Invalid amount. Please enter a number.")

			elif choice == "4":
				recipient_account = input("Enter recipient account number: ")
				recipient = bank.get_account(recipient_account)
				if recipient and recipient_account != bank.current_user.account_number:
					try:
						amount = float(input("Enter transfer amount: "))
						print(bank.current_user.transfer(amount, recipient))
					except ValueError:
						print("Invalid amount. Please enter a number.")
				else:
					print("Recipient account not found or invalid")
			elif choice == "5":
				bank.current_user = None
				print("Logged out")
			else:
				print("Invalid option")

if __name__ == "__main__":
	main()