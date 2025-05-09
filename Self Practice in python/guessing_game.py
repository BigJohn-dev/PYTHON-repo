# Guessing game in Python language

import random
print(random.randrange(0, 11))

print(' __- WELCOME TO GUESSING GAME -__ ')
print("Enter any digit to guess what's on the computer's mind...")

number = ((int)(input('\nEnter any number from 1 to 10: ')))

if number < 0 & number > 10:
	print('Invalid input')

else if number == random:
	print('You are correct')

else if number < random:
	print('Number is too low')

else:
	print('Number is too high')