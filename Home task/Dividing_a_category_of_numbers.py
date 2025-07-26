# Dividing a category of numbers

def categorize_numbers(numbers, divisor):
	if divisor == 0:
		raise ValueError("No divisible number found")

	return [num for num in numbers if num % divisor == 0]

print(categorize_numbers(10, 15, 21, 30}, -3))

