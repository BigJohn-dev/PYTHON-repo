# Add digits from a number

userInput = (input('Enter a number between 1 and 10,000: '))

number = int(userInput)

total = 0

while number > 0:
	total += number % 10
	number //= 10

print(total)

