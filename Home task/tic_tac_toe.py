#TIC_TAC_TOE GAME

def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 9)

def check_winner(board, player):
	for row in board:
		if all(cell == player for cell in row):
			return True

	for column in range(3):
		if all(board[row][column] == player for row in range(3)):
			return True

	if all(board[i][i] == player for i in range(3)):
        	return True
	if all(board[i][2 - i] == player for i in range(3)):
		return True
	return False

def is_board_full(board):
	return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
	board = [[" " for _ in range(3)] for _ in range(3)]
	current_player = "X"

print("Welcome to Tic-Tac-Toe!")
print("Enter row (0-2) and column (0-2) separated by a space (e.g., '1 1' for center).")

while True:
	print(print_board)
	try:
		row, column = map(int, input(f"Player {current_player}, enter row and column: ").split())
		if row not in range(3) or column not in range(3):
			print("Row and column must be between 0 and 2.")
			continue
		if board[row][column] != " ":
			print("That spot is already taken! Try again.")
			continue
	except ValueError:
		print("Invalid input! Enter two numbers separated by a space.")
		continue

		board[row][column] = current_player
		if check_winner(board, current_player):
			print_board(board)
			print(f"Player {current_player} wins!")
			break
		if is_board_full(board):
			print_board(board)
			print("It's a draw!")
			break

		current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
	while True:
		tic_tac_toe()
		if not play_again():
			print("Thanks for playing!")
			break