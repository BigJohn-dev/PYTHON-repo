# Tic-tac-toe
print('\nPYTHON GAMES.')
print('\n...starting game')


board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"
winner = None
running_game = True


def print_board(board):
	print(f"{board[0]} | {board[1]} | {board[2]}")
	print("----------")
	print(f"{board[3]} | {board[4]} | {board[5]}")
	print("----------")
	print(f"{board[6]} | {board[7]} | {board[8]}")


def player_input(board):
	global current_player
	while True:
		try:
			choice = int(input(f"\nPlayer {current_player}, Enter a number (1-9): "))
			if choice >= 1 and choice <= 9 and board[choice - 1] == " ":
				board[choice - 1] = current_player
				break
			else:
				print("Invalid input or spot already taken!")
		except ValueError:
			print("Please enter a valid number (1-9)!")


def horizontal_win(board):
	global winner
	if board[0] == board[1] == board[2] and board[0] != " ":
		winner = board[0]
		return True
	elif board[3] == board[4] == board[5] and board[3] != " ":
		winner = board[3]
		return True
	elif board[6] == board[7] == board[8] and board[6] != " ":
		winner = board[6]
		return True
	else:
		return False


def vertical_win(board):
	global winner
	if board[0] == board[3] == board[6] and board[0] != " ":
		winner = board[0]
		return True
	elif board[1] == board[4] == board[7] and board[1] != " ":
		winner = board[1]  # Fixed: was board[3]
		return True
	elif board[2] == board[5] == board[8] and board[2] != " ":
		winner = board[2]
		return True
	else:
		return False


def diagonal_win(board):
	global winner
	if board[0] == board[4] == board[8] and board[0] != " ":
		winner = board[0]
		return True
	elif board[2] == board[4] == board[6] and board[2] != " ":
		winner = board[2]
		return True
	else:
		return False


def check_tie(board):
	global running_game
	if " " not in board and not (horizontal_win(board) or vertical_win(board) or diagonal_win(board)):
		print_board(board)
		print("\nIt's a tie!")
		print("welldone")
		running_game = False
		return True
	else:
		return False


def check_for_winner(board):
	global running_game
	if horizontal_win(board) or vertical_win(board) or diagonal_win(board):
		print_board(board)
		print(f"\nThe winner is player {winner}!")
		print("Sharp...")
		running_game = False
		return True
	else:
		return False


def switch_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"  



while running_game:
	print_board(board)
	player_input(board)
	if check_for_winner(board) or check_tie(board):
		break
	switch_player()