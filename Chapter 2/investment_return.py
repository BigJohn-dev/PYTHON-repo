# 7% investment return

print(' _- INVESTMENT RETURN -_ ')

principal = (int)(input('\nEnter original amount invested: '))
rate = (int)(input('Enter annual rate of return: '))
years = (int)(input('Enter number of years: '))

Rate = rate / 1200
amount = principal * (1 + Rate) ** years

print('The amount on deposit at the end of the years: $', amount)