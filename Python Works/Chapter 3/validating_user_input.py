# Validating User Input



passes = 0
failures = 0
number = 'null'

for user_input in range (10):
	number = int(input('Enter number 1 or 2: '))

	if number == 1 or number == 2:
		passes += 1

	else:
		failures += 1


print('Passed: ', passes)
print('Failed: ', failures)