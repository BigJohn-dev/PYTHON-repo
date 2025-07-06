# printing the factorial of a number
print("The factorial of numbers")
number = int(input("Enter number: "))
result = 1
for i in range(1, number + 1):
    result *= i

print(f"Factorial of {number} is {result}")