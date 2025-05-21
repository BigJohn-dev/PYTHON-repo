# Dividing a category of numbers

def categorize_numbers(numbers, divisor):
	divisibles = []
	for number in numbers:
		if number % divisor == 0:
			divisibles.append(number)

	if divisibles != 0:
		return divisibles
		
	raise ValueError 

print(categorize_numbers([10, 15, 21, 30], 5))
