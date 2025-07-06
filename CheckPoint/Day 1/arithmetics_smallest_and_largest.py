# find the value of the smallest and largest in an arithmetic problem

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

add = number1 + number2 + number3
print(f"The sum of {number1}, {number2} and {number3} is: {add}")

product = number1 * number2 * number3
print(f"The product of {number1}, {number2} and {number3} is: {product}")

average = (number1 + number2 + number3) / 3
print(f"The average of {number1}, {number2} and {number3} is: {average}")

maximum = number1
if number2 > maximum:
    maximum = number2
if number3 > maximum:
    maximum = number3

minimum = number1
if number2 < minimum:
    minimum = number2
if number3 < minimum:
    minimum = number3

print(f"The maximum of {number1}, {number2} and {number3} is: {maximum}")
