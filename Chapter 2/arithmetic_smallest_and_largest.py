# Arithmetic smallest and largest

a = (int)(input('Enter first number: '))
b = (int)(input('Enter second number: '))
c = (int)(input('Enter third number: '))

sum = a + b + c
average = sum / 3
product = a * b * c
smallest = min(a, b, c)
largest = max(a, b, c)

print('\nThe sum of all three input is ', sum)
print('The average of all three input is ', average)
print('The product of all three input is ', product)
print('The smallest of all three input is ', smallest)
print('The largest of all three input is ', largest)