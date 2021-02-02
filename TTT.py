# TicTacToe

class TicTacToe():
	""" A Class for built for playing a two player Tic Tac Toe game """

	def __init__(self):
		print('Lets play Tic Tac Toe')
		print("'X' plays first\n")

		self.turn = 1
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

	def game_loop(self):
		board = self.board
		turn = self.turn

		while True:
			self.display_guide()
			self.display_board(turn, board)

			board = self.play_X_or_O(turn, board)
			if board == []:
				break
			flag, winner = self.check_win(board)

			if flag:
				self.display_board(2, board)
				print(f'Nice work {winner}')
				break
			if winner == 'Draw':
				self.display_board(2, board)
				print('Thats a draw folks')
				break

			if turn == 1:
				turn = 0
			else:
				turn = 1

	def display_board(self, turn, board):
		if turn == 1:
			marker = 'X'
		else:
			marker = 'O'

		if turn == 2:
			print('Game Over')
		else:
			print(f"It is {marker}'s turn.")

		top_row = " " + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]
		middle_row = board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2]
		bottom_row = board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2]

		print(top_row,'\n-----------\n', middle_row, '\n-----------\n', bottom_row)

	def check_win(self, board):
		win = ['XXX', 'OOO']
		for x in range(3):
			# Check for row win
			if ''.join(board[x]) in win:
				return True, board[x][0]

			# Check for column winner
			column  = board[0][x] + board[1][x] + board[2][x]
			if column in win:
				return True, board[0][x]

		# Check Diag's
		diag1 = ''.join([board[i][i] for i in range(3)])
		diag2 = ''.join([board[i][j] for i, j in enumerate(range(2, -1, -1))])
		if diag1 in win:
			return True, diag1[0]
		if diag2 in win:
			return True, diag2[0]

		# Check for draw
		board_values = "".join(["".join(x) for x in board])
		if " " not in board_values:
			return False, 'Draw'

		return False, ''

	def display_guide(self):
		guide_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

		top_row = " " + guide_board[0][0] + ' | ' + guide_board[0][1] + ' | ' + guide_board[0][2]
		middle_row = guide_board[1][0] + ' | ' + guide_board[1][1] + ' | ' + guide_board[1][2]
		bottom_row = guide_board[2][0] + ' | ' + guide_board[2][1] + ' | ' + guide_board[2][2]
		print('Using the below grid, Enter the number of the square \nyou would like to play in\n')
		print(top_row, '\n-----------\n', middle_row, '\n-----------\n', bottom_row, '\n')
		
	def play_X_or_O(self, turn, board):
		if turn == 1:
			marker = 'X'
		else:
			marker = 'O'

		while True:
			print("Hit 'q' at any time to quit the game.") 
			pos = input('In what position would you like to play: ')
			if pos == 'q':
				return []

			if pos in [str(x) for x in range(1, 10)]:
				print('\n')
				row = (int(pos) - 1) // 3
				col = (int(pos) - 1) % 3
				if board[row][col] == " ":
					board[row][col] = marker
					return board
				else: 
					print('That spot has already been taken')
					print('Choose a different locations')
			else: 
				print('You must enter a number between 1-9')
				print('Give it another try\n')


if __name__ == "__main__":
	# Make a game instance, and run the game loop
	TTT = TicTacToe()
	TTT.game_loop()


