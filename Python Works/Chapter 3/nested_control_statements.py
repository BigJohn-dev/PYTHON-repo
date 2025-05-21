# Nested Control Statements

largest_number = 0
second_largest_number = 0

for count in range (1, 11):
	number = int(input('Enter a number: '))
	
	if number > largest_number:
		second_largest_number = largest_number
		largest_number = number

if number > second_largest_number and number != largest_number:
	second_largest_number = number

print(f'The largest number is {largest_number}')
print(f'The second largest number is {second_largest_number}')