# Semicolon Payroll

class Semicolon_payroll:

	def __init__(self):
		self.displayPayroll = []

	def add_employee(self, name, hours_worked, pay_rate):
		if name == " ":
			return "Enter employee name"
		if name not in self.displayPayroll:
			gross_pay = hours_worked * pay_rate
			federal_tax = self.federal_withholding(gross_pay)
			state_tax = self.state_withholding(gross_pay)
			net_pay = gross_pay - federal_tax - state_tax
			self.displayPayroll.append({"Name:": name, "Number of hours worked in a week:": hours_worked, "Hourly pay rate:": pay_rate, "Federal Withholding:": federal_withholding, "State Withholding:": state_withholding})
			return "New employee payroll added"
		return "Employee's details already exist"

	def view_employee(self):
		if not self.displayPayroll:
			return "<<< No employee details added >>>"
		result = "\nLIST OF SEMICOLON'S EMPLOYEES PAYROLL:\n"
		for i, display in enumerate(self.displayPayroll, 1):
			result += f"{i}. {displayPayroll['name'], ['hours_worked'], ['pay_rate'], ['federal_tax_rate'], ['state_tax_rate']}\n"
		return result

	def update_payroll(self, index):
		if 1 <= index <= len(self.displayPayroll):
			employee_payroll = self.displayPayroll.pop(index - 1)
			return f"Employee '{employee_payroll['name']}' deleted, recreate profile"
		return "You sure say you add am?!!"

	def federal_withholding(amount):
		if amout < 0:
			return "Invalid pay amount"
		else:
			result = amount * 0.2
			federal_withholding += result
			return federal_withholding
			return f"Your Federal Withholding (20.0%): ${federal_withholding}"

	def state_withholding(amount):
		if amout < 0:
			return "Invalid pay amount"
		else:
			result = amount * 0.09
			state_withholding += result
			return f"Your State Withholding (9.0%): ${state_withholding}"


def main():
	semicolon_payroll = Semicolon_payroll()
	while True:
		print("\nWELCOME TO SEMICOLON AFRICA")
		print("\nSEMICOLON'S PAYROLL PAGE")
		print("...keeping track of your employee's pays")
		payroll_menu = '''
		
...select an option
=============================
1. Add an Employee payroll
2. View all Employees payroll
3. Update an Employee payroll
4. Exit
=============================
'''
		print(payroll_menu)
		selected = input("Enter your choice (1-4): ")

		if selected == "1":
			print("\nADD AN EMPLOYEE PAYROLL")
			name = input("Enter Employee name: ")
			hours_worked = float(input("Enter Number of Hours Worked: "))
			if hours_worked > 200:
				print("Invalid work hour")
			else:
				pay_rate = float(input("Enter pay rate: "))
				Gross_pay = hours_worked * pay_rate
				print(Semicolon_payroll.add_employee(name, hours_worked, pay_rate, Gross_pay))
				print(Semicolon_payroll.federal_withholding(Gross_pay))
				print(Semicolon_payroll.state_withholding(Gross_pay))

		elif selected == "2":
			print("\nVIEW ALL EMPLOYEES PAYROLL")
			print(semicolon_payroll.view_employee())

		elif selected == "3":
			print("\nUPDATE AN EMPLOYEE PAYROLL")
			number = input("Enter the name of employee: ")
			print(semicolon_payroll.update_payroll())
			try:
				payroll_num = int(input("Enter payroll number to edit: "))
				print(semicolon_payroll.update_payroll(payroll_num))
			except ValueError:
				print("Invalid input, please enter a number")

		elif selected == "4":
			print("...thank you for using our app!")
			print("...@semicolon.africa")
			break
		else:
			print("Instructions are clear, options is from 1 to 4...")

if __name__ == "__main__":
	main()