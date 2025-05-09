# separating the digits in an integer

number = (int)(input('Enter a five digit number: '))

num1 = (number // 10000) % 10
num2 = (number // 1000) % 10
num3 = (number // 100) % 10
num4 = (number // 10) % 10
num5 = (number // 1) % 10

print('\nThe separated version')
print(num1, ' ', num2, ' ', num3, ' ', num4, ' ', num5)