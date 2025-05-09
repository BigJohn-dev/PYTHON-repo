;# Evaluating the strength of a user's password

print(' _- CHECK PASSWORD STRENGTH -_ ')

user_name = input('Enter your name: ')
password = input('Enter your password: ')

count = 0
for length in password:
	count += 1


if count < 8:
	print('Password is very weak')

elif count == 8:
	print('Password is weak')

elif   8 > count <= 16:
	print('Password is strong')

else:
	print('Password is very strong')

