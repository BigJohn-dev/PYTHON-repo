# Arithmetic, Smallest and Largest

count = 0
sum = 0
largest = 0
smallest = 0
product = 1

while count < 4:
	number = int(input('Enter a number: '))
	sum += number
	product *= number
	count += 1

average = sum / 4

if number > largest:
	largest = number

if number < smallest:
	smallest = number


print(f'The total sum is {sum} and the largest is {largest} and smallest is {smallest}')
print(f'The product is {product} and the average {average}')