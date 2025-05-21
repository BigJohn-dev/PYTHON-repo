# Investment Return

principal = int(input('Enter the principal amount: '))
rate = int(input('Enter the annual rate: '))
years = int(input('Enter the number of years to payback: '))

Rate = rate / 1200 

for returns in range (1, 31):
	amount = principal * (1 + Rate) ** years 
	print(returns, amount)