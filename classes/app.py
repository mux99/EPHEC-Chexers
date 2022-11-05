from bin.fcts import screen_to_board, board_to_screen, get_starting_pos, validate_click
from classes.piece import Piece

import pyglet

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
		self._clicked_coord = None #value is a (x, y ,z) coords of a selected tile. if selected display possible moves, takes

		self.valid_moves = [] #coords of valid tiles to move to (depending of selected tile)
		self.valid_takes = [] #coords of pieces that can be taken (depending of selected tile)

		self.board_size = 8

		#textures
		self._textures = {}

		#scaling
		self._tile_height = 1

	def reset(self):
		pass

	def set_textures(self, textures, scale=1):
		self._textures = textures
		self._scale = scale

	def rescale(self,height):
		self._tile_height = height / 6.25
		for i in self._pieces:
			i.scale = height / 2000

	def draw_textures(self,window):
		#draw pieces
		for i in self._pieces:
			i.draw(self._tile_height)

	"""
		fill board with pieces at their correct starting positions
	"""
	def init_board(self):
		pos = get_starting_pos(8)
		for i in range(len(pos[0])):
			self._pieces.append(Piece(x=pos[0][i][0], y=pos[0][i][1], z=pos[0][i][2], color="white", texture=self._textures["white"], scale=self._scale))
			self._pieces.append(Piece(x=pos[1][i][0], y=pos[1][i][1], z=pos[1][i][2], color="black", texture=self._textures["black"], scale=self._scale))


	"""
		receive coords of a click on screen and takes action on it:
		- ignore coords out of bounds
		- translate screen coords to game coords (fcts.py screen_to_board(x,y))
		- on first click on a tile, hold coords
		- on second make move if legal
		- change self.player at the end of the turn(when a move is done)
	"""
	def click(self, screen_x, screen_y):
		"""coords = screen_to_board(screen_x,screen_y,self._tile_height) # incomplete, needs some tweaks and doesn't work for now
																		#will need to look at it later
		tile_has_piece = self.has_pieces([coords])[0]
		#print(self.validate_click(coords[0], coords[1], coords[2]))
		if not self.validate_click(coords[0], coords[1], coords[2]):
			print("Invalid coords")
			return
		if self._click == 0:
			if tile_has_piece:
				piece = [obj.coord == coords for obj in self._pieces][0]
				if not (piece.color == "white" and self._player == 1) or not (piece.color == "black" and self._player == 2):
					return
				self._hold = piece
				self._click = 1
				return
		if not tile_has_piece:
			self.list_moves()
			if coords in self.valid_moves:
				self.move(coords[0], coords[1], coords[2])
				self._click = 0
				if self._player:
					self._player = 0
				else:
					self._player = 1
				return"""




		
		click_coords = screen_to_board(screen_x,screen_y,self._tile_height)

		#discard invalid clicks
		if not validate_click(click_coords):
			print(click_coords,"is invalid")
			return

		#select new piece
		if self.is_pieces(click_coords) and self._clicked_coord == None:
			print("select")
			self._clicked_coord = click_coords

		#move selected
		elif not self.is_pieces(click_coords) and self._clicked_coord != None:
			print("move")
			self.move(self._clicked_coord,click_coords)
			self._clicked_coord = None

		#select other piece
		elif self.is_pieces(click_coords) and self._clicked_coord != None:
			print("reselect")
			self._clicked_coord = click_coords



		print(click_coords,self._clicked_coord)
		
	"""
		receive coords (x,y,z),
		returns a boolean:
		True if a piece is in that place, False otherwise
	"""
	def is_pieces(self, coord):
		for piece in self._pieces:
			if coord == piece.coord:
				return True
		return False

	def move(self,curent,new):
		for piece in self._pieces:
			if piece.coord == curent:
				piece.coord = new