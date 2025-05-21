# Brute-Force Computing: Pythagorean Triples

a = (input('Enter first value: '))
b = (input('Enter second value: '))
c = (input('Enter third value: '))

value = int(max(a, b, c))

for a in range(1, value + 1):
	for b in range(a, value + 1):
		for c in range(b, value + 1):
			if a**2 + b**2 == c**2:
				print(f'Pythagorean triple: ({a}, {b}, {c})')