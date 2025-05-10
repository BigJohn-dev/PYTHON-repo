# Table of Square and Cubes

print('number\tsquare\tcube')


for i in range(0, 3):
	for j in range(0, 3):
		print(f'{i:>5}', i * i, i * i * i, end = (f'{i:>2}'))
	print(' ')