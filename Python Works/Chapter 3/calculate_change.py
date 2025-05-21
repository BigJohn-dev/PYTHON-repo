# Calculate Change Using Fewest Number of Coins

purchase_price = float(input('Enter price of item (a dollar or less): '))
amount_paid = float(input('Enter amount paid: '))

change = int((amount_paid - purchase_price)) * 100

change_in_quarters = (change // 25) % 25
change_in_dimes = (change_in_quarters // 10) % 10
change_in_nickels = (change_in_dimes // 5) % 5

change_in_pennies = change_in_nickels

print(f'Your change is: {change_in_quarters} quarters, {change_in_dimes} dimes, {change_in_pennies} pennies')

