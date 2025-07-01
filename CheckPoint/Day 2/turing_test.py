# Playing role of independent computer

problem = input("What is your problem?: ")
response = input('Have you had this problem before?: ')
if response.lower() == 'yes':
    print('Well, you have it again.')
elif response.lower() == 'no':
    print('Well, you have it now.')
else:
    print('Invalid input.')
