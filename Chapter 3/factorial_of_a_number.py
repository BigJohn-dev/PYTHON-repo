# Factorial of a number

n = int(input('Enter a number: '))

result = 1

for fact in range(1, n + 1):
	result *= fact
	
print(f'The factorial of {n} is {result}')






