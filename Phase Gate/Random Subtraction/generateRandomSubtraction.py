# Generate Random Subtraction Questions
import random

number1 = random.randrange(50, 100)
number2 = random.randrange(1, 50)

print("What is ", number1, "-", number2, "?: ")
user_input = input()

answer = number1 - number2

if user_input == answer:
	print("You are correct")
	count += 1
else:
	print("You are wrong")
	counter += 1

print("You got ", count, "correct answers")
print("You got ", counter, "wrong answers")