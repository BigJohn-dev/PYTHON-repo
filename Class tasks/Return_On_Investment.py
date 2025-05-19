# ROI


principal = int(input('Enter the principal amount: '))
rate = int(input('Enter the annual rate: '))
years = int(input('Enter the number of years to payback: '))

Rate = rate / 100 
amount = principal * Rate

for returns in range (1, years+1):
	for count in range (1):
		 print(f'{returns}, {principal + (amount * returns):,.2f}')
	print()