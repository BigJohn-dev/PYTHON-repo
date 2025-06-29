# Creating a Banking application

class ATM:

	def __init__(self, balance = 0.0):
		self.balance = balance
		self.transactions = []

	def deposit_money(self, amount):
		if amount > 0:
			self.balance += amount
			self._log_transaction("Deposit", amount, "Deposit fee N0.0")
			return f"Deposited N{amount:,.2f}. New balance: N{self.balance:,.2f}"
		else:
			return "Invalid deposit amount"

	def withdraw_money(self, amount):
		if amount > 20000:
			return "Exceeded withdrawal limit "
		elif amount > 0 and amount <= 20000 and self.balance >= amount:
			self.balance -= amount + 100
			self._log_transaction("Withdrawal", amount, "Withdrawal fee N 100.0" )
			return f"\nTransaction successful \nWithdrawal amount: N{amount:,.2f}. \nWithdrawal fee: N 100. \nNew balance: N{self.balance:,.2f}."
		else:
			return "Invalid withdrawal amount or insufficient funds"

	def check_balance(self):
		return  f"Balance: N{self.balance:,.2f}"

	def _log_transaction(self, Category, amount, fee):
		transaction = {
		"Category": Category,
		"Amount" : amount,
		"Charges" : fee,
		"Balance" : self.balance
		}
		self.transactions.append(transaction)

	def history(self):
		result = "\nYOUR TRANSACTION HISTORY"
		return self.transactions
	
def main():
	atm = ATM()
	while True:
		print("\n WELCOME TO SEMICOLON BANK...")		
		print("1. Deposit \n2. Withdraw  \n3. Check Balance \n4. Transaction History \n5. Logout")
		choice = input("\nChoose an option: ")

		if choice == "1":
			try:
				amount = float(input("Enter deposit amount: "))
				print(atm.deposit_money(amount))
			except ValueError:
				print("Invalid amout. Please enter a number.")

		elif choice == "2":
			try:
				amount = float(input("Enter withdrawal amount: "))
				print(atm.withdraw_money(amount))
			except ValueError:
				print("Invalid amount. Please enter a number.")

		elif choice == "3":
				print(atm.check_balance())

		elif choice == "4":
				print("YOUR TRANSACTION HISTORY")
				print(atm.history())
		
		elif choice == "5":
				atm.current_user = None
				print("...thank you for banking with us. Logged out")
				break
									

if __name__ == "__main__":
	main()