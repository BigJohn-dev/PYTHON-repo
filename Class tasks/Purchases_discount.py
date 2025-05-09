# Purchases discount

"""
PSUEDO CODE

prompt user to enter purchase amount
 if the purchase amount is between 1_000 and 10_000 give a 5% discount
  elif the purchase amount is between 10_000 and 50_000 give a 10% discount
   else the purchase amount is 50_000 and above give a 20% discount
"""

purchase_amount = int(input('Enter your total spendings: '))

if purchase_amount >= 1000 and purchase_amount <= 10000:
	discount = purchase_amount * 0.05
	print(f'Your discount is ${discount}')

elif purchase_amount > 10000 and purchase_amount <= 50000:
	discount = purchase_amount * 0.10
	print(f'Your discount is ${discount}')

else:
	discount = purchase_amount * 0.20
	print(f'Your discount is ${discount}')

total_fees_after_discount = purchase_amount - discount
print(f'Your total payment after discount is ${total_fees_after_discount:,.2f}')