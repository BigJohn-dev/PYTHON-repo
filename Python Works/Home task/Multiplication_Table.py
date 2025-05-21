# Multiplication Table

print('\n\t\t\tMultiplication Table')

print('\n\t1\t2\t3\t4\t5\t6\t7\t8\t9')
print('-' * 75)

for j in range(1, 10):
	print(f"{j:>2}|\t{j}\t{j * 2}\t{j * 3}\t{j * 4}\t{j * 5}\t{j * 6}\t{j * 7}\t{j * 8}\t{j * 9}")