import random

print(' _- GUESS THE NUMBER -_ ')
print('...welcome')

guessNumber = random.randrange(1, 1001)
guess_count = 0

start_input = int(input('Enter 0 to start:'))
if start_input < 0 or start_input > 0:
	print('Recompile')
else:
	while True:
		userGuess = int(input('Guess my number between 1 and 1000 with the fewest guesses:'))
		guess_count += 1
		
		if userGuess <= 0 or userGuess > 1000:
			print('Invalid guess input')
		else:
			if(userGuess < guessNumber):
				print('Number is too low')
			elif(userGuess > guessNumber):
				print('Number is too high')
			else:
				print('Congratulation')

				respond = int(input('Press 5 to continue or 0 to quit: '))
				if respond == 0:
					print('Thanks for playing!')
					break
				elif respond == 5:
					guessNumber = random.randrange(1, 1001)
					print('\nNew game started!')
				else:
                			print('Invalid input, quitting game.')
                			break
		
if guess_count <= 10:
	print("Either you know the secret or you got lucky!")
else:
	print("You should be able to do better!")
