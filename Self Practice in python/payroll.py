# Employees Payroll

class payroll:

	def gross_pay(amount, time):
		grosspay = amount * time
		return grosspay

	def federalTax(amount):
		tax = amount * 0.20
		return tax

	def stateTax(amount):
		tax = amount * 0.09
		return tax

def main():

	print("WELCOME TO PAYROLL");
	
	name = input("\nEnter employee's name: ")

	time = float(input("Enter number of hours worked in a week: "))
	
	rate = float(input("Enter hourly pay rate: "))
	
	print(f"\nEmployee Name: {name}")
	print(f"Hours worked: {time}")
	print(f"Pay Rate: ${rate}")
	print(f"Gross Pay: ${payroll.gross_pay(time, rate)}")

	print("\nDeductions:");
	print(f"Federal Withholding (20.0%): ${payroll.federalTax(payroll.gross_pay(time, rate))}")
	print(f"Federal Withholding (9%): ${payroll.stateTax(payroll.gross_pay(time, rate))}")
	print(f"Total deductions: ${(payroll.stateTax(payroll.gross_pay(time, rate)) + payroll.federalTax(payroll.gross_pay(time, rate)))}")

	print(f"\nNet Pay: ${(payroll.gross_pay(time, rate) - (payroll.stateTax(payroll.gross_pay(time, rate)) + payroll.federalTax(payroll.gross_pay(time, rate))))}")
	
if __name__ == "__main__":
	main()