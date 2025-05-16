# Adding digits using the function

def sum_digits(number):
	total = 0
	while number > 0:
		total += number % 10
		number //= 10
	return total


print(sum_digits(4567))