# Sort in ascending order

print(' __- ASCENDING ORDER -__ ')

a = float(input('Enter first decimal number: '))
b = float(input('Enter second decimal number: '))
c = float(input('Enter third decimal number: '))
"""
numbers = [a, b, c]
numbers.sort()
print(numbers)

"""

# Determine and display numbers in increasing order
if a <= b and a <= c:
    smallest = a
    if b <= c:
        middle = b
        largest = c
    else:
        middle = c
        largest = b
elif b <= a and b <= c:
    smallest = b
    if a <= c:
        middle = a
        largest = c
    else:
        middle = c
        largest = a
else:
    smallest = c
    if a <= b:
        middle = a
        largest = b
    else:
        middle = b
        largest = a

print(f"Numbers in increasing order: {smallest}, {middle}, {largest}")