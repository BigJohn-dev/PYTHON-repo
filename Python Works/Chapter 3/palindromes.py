# Palindrome numbers

numbers = int(input('Enter a five-digit number: '))

rev1 = (numbers // 10000) % 10
rev2 = (numbers // 1000) % 10
rev3 = (numbers // 100) % 10
rev4 = (numbers // 10) % 10
rev5 = (numbers // 1) % 10

temp = rev1, ' ', rev2, ' ', rev3, ' ', rev4, ' ', rev5
reverse = rev5, ' ', rev4, ' ', rev3, ' ', rev2, ' ', rev1

if temp == reverse:
	print('Number is a palindrome')
else:
	print('Number is not a palindrome')