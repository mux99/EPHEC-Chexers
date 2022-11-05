from bin.fcts import screen_to_board, board_to_screen, get_starting_pos
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
		self._hold = None #value is a (x, y ,z) coords of a selected tile. if selected display possible moves, takes
		self._click = 0 #keeps track of the click

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
		#print(screen_to_board(screen_x,screen_y,self._tile_height))
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
		coords = screen_to_board(screen_x,screen_y,self._tile_height)
		print(coords,self._hold)
		
		if self._hold == None:
			self._hold = coords
		else:
			self.move(self._hold[0],self._hold[1],self._hold[2],coords[0],coords[1],coords[2])
			self._hold = None
		#self.list_moves() update valid moves on first click (use list to validate move on second click)
		#use self.move(x,y,z) to move the piece when necessary
		pass

	"""
		return True if the coordinate are valid, False if not
		usable tiles coords follow a pattern like that:
		if x = 0 | 1 -> y = 0 to -7
		if x = 2 | 3 -> y = -1 to -8
		if x = 4 | 5 -> y = -2 to -9
		if x = 6 | 7 -> y = -3 to -10
		z isn't relevant since it depends on the value of x and y at the same time
		can't really check that without a big match statement with hardcoded values or lots of ifs :/
		works at least i guess ¯\_(ツ)_/¯ 
	"""
	@staticmethod
	def validate_click(x, y, z):
		if (x + y + z) != 0:
			print("Illegal Coordinates")
			return False
		match x:
			case 0 | 1:
				if -7 <= y <= 0:
					return True
				return False
			case 2 | 3:
				if -8 <= y <= -1:
					return True
				return False
			case 4 | 5:
				if -9 <= y <= -2:
					return True
				return False
			case 6 | 7:
				if -10 <= y <= -3:
					return True
				return False
			case other:
				return False

	"""
			list all coords the selected piece can move to
			!! keep promoted in mind !!
			!! keep 'infinite' board in mind !! (that's for later)
	"""
	def list_moves(self):
		if self._hold.promotion:
			pass #undefined for now
		else:
			all_moves = [(self._hold.x + 2, self._hold.y, self._hold.z), (self._hold.x - 2, self._hold.y, self._hold.z), (self._hold.x, self._hold.y, self._hold.z + 2), (self._hold.x, self._hold.y, self._hold.z - 2)]
			check_moves = has_pieces(self, all_moves)
			for m in all_moves:
				if not check_moves[all_moves.index(m)]:
					del all_moves[all_moves.index(m)]


	"""
		list all possible takes from selected piece to given coords
		!! only enemy !!
	"""
	def list_takes(self, x, y, z):
		pass


	"""
		receive a list of coords (x,y,z),
		returns a list of same length containing booleans:
		True if a piece is in that place, False otherwise
	"""
	def has_pieces(self, p):
		bool_list = []
		for coord in p:
			for piece in self._pieces:
				if coord == piece.coord:
					bool_list.append(True)
					break
			else:
				bool_list.append(False)
		return bool_list


	"""
		change coords of the selected piece
	"""
	def move(self, x, y, z, new_x, new_y, new_z):
		for piece in self._pieces:
			if (piece.x == x and piece.y == y) and piece.z == z:
				piece.x = new_x
				piece.y = new_y
				piece.z = new_z
				return
