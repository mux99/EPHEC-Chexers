from fcts import screen_to_board

class App():
	"""
		---TBD---
	"""
	def __init__(self):
		self._pieces = [] #list all pieces on the board
		self._player = 1 #store the current player (1 white| 2 black)
		self.pause = False #will be used to toggle the pause menu display and deactivate clicking on pieces
		self._score_P1 = 0 #scoring system TBD
		self._score_P2 = 0 #scoring system TBD
		self._hold = None #value is a (x, y ,z) coords of a selected tile. if selected display possible mooves, takes

		self.valid_mooves = [] #coords of valid tiles to move to (depending of selected tile)
		self.valid_takes = [] #coords of pieces that can be taken (depending of selected tile)


	"""
		receive coords of a click on screen and takes action on it:
		- ignore coords out of bounds
		- translate screen coords to game coords (fcts.py screen_to_board(x,y))
		- on first click on a tile, hold coords
		- on second make move if legal
		- change self.player at the end of the turn(when a move is done)
	"""
	def click(self, screen_x, screen_y, screen_max_x, screen_max_y):

		#self.list_mooves() update valid mooves on first click (use list to validate move on second click)
		#use self.move(x,y,z) to move the piece when necesary
		pass


	"""
		list all coords the selected piece can move to
		!! keep promoted in mind !!
		!! keep 'infinite' board in mind !! (that's for later)
	"""
	def list_mooves(self):
		#use self.is_pieces() to check multiple cases at once
		pass


	"""
		list all possible takes form selected piece to given coords
		!! only enemy !!
	"""
	def list_takes(self,x,y,z)
		pass


	"""
	receive a list of coords (x,y,z),
	rerurn a list of same lenght containig a boolean:
		True if a piece is in that place, False otherwise

	"""
	def is_pieces(p):
		pass


	"""
		change coords of the selected tile
	"""
	def moove(x, y, z):
		pass