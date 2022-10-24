from bin.fcts import screen_to_board, get_starting_pos
from classes.piece import Piece

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

		self.board_size = 8

		#textures
		self._white = None
		self._white_queen = None
		self._black = None
		self._black_queen = None
		self._scale = 1

	"""
		reset game state to default
	"""
	def reset(self):
		pass


	"""
		set textures (pyglet.image) for game pieces
	"""
	def set_textures(self,white_texture, black_texture, scale=1):
		self._white = white_texture
		#self._white_queen = white_queen_texture
		self._black = black_texture
		#self._black_queen = black_queen_texture
		self._scale = scale

	def draw_textures(self):
		for i in self._pieces:
			i.draw()


	"""

	"""
	def init_board(self):
		pos = get_starting_pos(8)
		for i in range(len(pos[0])):
			self._pieces.append(Piece(x=pos[0][i][0], y=pos[0][i][1], z=pos[0][i][2], color="white", texture=self._white, scale=self._scale))
			self._pieces.append(Piece(x=pos[0][i][0], y=pos[0][i][1], z=pos[0][i][2], color="black", texture=self._black, scale=self._scale))


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
	def list_takes(self, x, y, z):
		pass


	"""
	receive a list of coords (x,y,z),
	rerurn a list of same lenght containig a boolean:
		True if a piece is in that place, False otherwise

	"""
	def is_pieces(self, p):
		pass


	"""
		change coords of the selected tile
	"""
	def moove(self, x, y, z):
		pass