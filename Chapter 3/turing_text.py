# Turing Text

print(' _- MEDICAL DIAGNOSIS -_ ')

user_first_response = input('\nWhat is your problem? ')

user_second_response = input('\nHave you had this problem before (yes or no)? ')


if user_second_response == 'yes' or user_second_response == 'Yes' or user_second_response == 'yEs' or user_second_response == 'yeS' or user_second_response == 'YES' or user_second_response == 'YEs':
	print('Well, you have it again.', end = '')

if user_second_response == 'no' or user_second_response == 'NO' or user_second_response == 'nO' or user_second_response == 'No':
	print('Well, you have it now.')

