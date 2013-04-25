class Piece:
	EX, OH, BLANK = 'X', 'O', ' '
class Spot:
	def __init__(self):
		self.piece = Piece.BLANK
	def __str__(self):
		return self.piece
	def move (self, new_piece):
		self.piece = new_piece
	def here(self):
		return self.piece
class Board:
	"""
	0|1|2
	3|4|5
	6|7|8
	"""
	possible_wins = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8], #vertical wins
		[0, 3, 6], [1, 4, 7], [2, 5, 8], #horizontal wins
		[0, 4, 8], [2, 4, 6] #diagonal wins
	]
	def __init__(self):
		self.current = Piece.EX
		self.opponent = Piece.OH
		self.board = list()
		for _ in range(9):
			self.board.append(Spot())
	def switchTurn(self):
		temp = self.current
		self.current = self.opponent
		self.opponent = temp
	def makeMove(self, spot): 
		if (self.pos(spot).here() is not Piece.BLANK):
			return -1
		else :
			self.board[spot].move(self.current)
			self.switchTurn()
	def finished(self):
		for a,b,c in Board.possible_wins:
			if (self.pos(a).here() is self.pos(b).here() is self.pos(c).here() and self.pos(a).here() is not Piece.BLANK):
				return True
		return False
	def pos(self, num):
		return self.board[num]
	def __str__(self):
		board_str = "\n{0}|{1}|{2}\n-----\n{3}|{4}|{5}\n-----\n{6}|{7}|{8}\n"
		return board_str.format( 
		 self.pos(0), self.pos(1), self.pos(2), 
		 self.pos(3), self.pos(4), self.pos(5), 
		 self.pos(6), self.pos(7), self.pos(8))
	


def main():
	print "Welcome to Tic-Tac-Toe"
	board = Board()
	while (not board.finished()):
		print board
		print "It is {0}'s turn".format(board.current)
		move = input('Where would you like to go? : ')
		if (move == -1):
			continue
		board.makeMove(move)
	print "Game Over"
	print "Player {0} wins!".format(board.opponent)

main()

