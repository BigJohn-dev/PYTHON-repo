# Use a loop to find the two largest values of 10 numbers entered.

first_max = second_max = float('-inf')

for i in range(1, 11):
    number = int(input(f"Enter a value for number {i}: "))
    if number > first_max:
        second_max = first_max
        first_max = number
    elif number > second_max:
        second_max = number

print(f"The first largest number is: {first_max}")
print(f"The second largest number is: {second_max}")
