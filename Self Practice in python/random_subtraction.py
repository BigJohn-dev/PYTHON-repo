<<<<<<< HEAD
# Generate Random Subtraction Questions
import random

count = 0
counter = 0

for i in range(1, 11):
	number1 = random.randrange(50, 100)
	number2 = random.randrange(1, 50)

	for j in range(1, 3):
		print("What is ", number1, "-", number2, "?: ")
		user_input = input()

		answer = number1 - number2

		if user_input == answer:
			print("You are correct")
			count += 1
		elif user_input != answer:
			print("You are wrong")
			counter += 1

print("You got ", count, "correct answers")
=======
# Generate Random Subtraction Questions
import random

count = 0
counter = 0

for i in range(1, 11):
	number1 = random.randrange(50, 100)
	number2 = random.randrange(1, 50)

	for j in range(1, 3):
		print("What is ", number1, "-", number2, "?: ")
		user_input = input()

		answer = number1 - number2

		if user_input == answer:
			print("You are correct")
			count += 1
		elif user_input != answer:
			print("You are wrong")
			counter += 1

print("You got ", count, "correct answers")
>>>>>>> origin/main
print("You got ", counter, "wrong answers")