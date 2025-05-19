# Mortgage Calculator

"""
PSEUDO CODE
1. Display user-friendly welcome message
2. Ask the user to enter the loan amount 
3. Ask the user to enter the annual interest rate
4. Ask the user to enter the loan duration in years
5. Convert the annual interest rate to a monthly interest rate
6. Convert the loan duration in years to total number of months
7. Use the mortgage formula to calculate the monthly payment:
   Formula:
monthlypayment = principal * Rate * (1 + Rate) ** Duration / ((1 + Rate) ** Duration - 1)
8. Display the calculated monthly payment rounded to two decimal places
9. Display a closing message thanking the user

"""

print('\n__-- MORTGAGE CALCULATOR --__ ')
print('*********************************')

print('\n...the smarter way to mortgage planning...')
print('\nWhat monthly payment can I comfortably afford?')

print('===============================')
principal = (float)(input('\nHow much is your loan? '))

print('===============================')
rate = (float)(input('What is the annual interest rate? '))

print('===============================')
duration = (float)(input('How long to pay back your loan? '))

Rate = rate / 1200
Duration = duration * 12

monthlyPay = principal * Rate * (1 + Rate) ** Duration / ((1 + Rate) ** Duration - 1)
	
print('===============================')
print(f'Your monthly payment is: ${monthlyPay:.2f}')

print('\nNow you know....')
print('Thank you for using our Mortgage Calculator. We hope it helped you plan with confidence.')