# Nested loops
for row in range(1, 11):
	print('* ' * row)


for row in range(10, 0, -1):
	for column in range(0, row):
		print('*', end =' ')
	print()

for row in range(10):
	for column in range(row + 1):
		print(' ', end =' ')
	for column in range(row, 10):
		print('*', end =' ')
	print()


for row in range(10):
	for column in range(row, 10):
		print(' ', end =' ')
	for column in range(row + 1):
		print('*', end =' ')
	print()
