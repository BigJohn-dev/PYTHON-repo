# Separating the Digits in an Integer

numbers = int(input('Enter five digit number: '))
digits = []
for i in range (1,6):
    digits.append(numbers % 10)
    numbers //= 10

print(sorted(digits))