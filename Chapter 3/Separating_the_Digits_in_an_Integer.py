# Separating the Digits in an Integer

values = int(input('Enter five-digit number: '))

numbers = abs(values)

digits = []

if values == 0:
	digits.append(0)
else:
	while numbers > 0:
		digit = numbers % 10
		digits.append(digit)
		numbers //= 10  

digits = digits[::-1]
    
print(f'Numbers:{digits}')