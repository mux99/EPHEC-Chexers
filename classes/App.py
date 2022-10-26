from bin.fcts import screen_to_board, board_to_screen, get_starting_pos
from classes.piece import Piece

class App:
	"""
		---TBD---
	"""
	def __init__(self):
		self._pieces = {} #list all pieces on the board
		self._player = 1 #store the current player (1 white| 2 black)
		self.pause = False #will be used to toggle the pause menu display and deactivate clicking on pieces
		self._score_P1 = 0 #scoring system TBD
		self._score_P2 = 0 #scoring system TBD
		self._hold = None #value is a (x, y ,z) coords of a selected tile. if selected display possible moves, takes
		self._click = 0 #keeps track of how many times the player clicked

		self.valid_moves = [] #coords of valid tiles to move to (depending of selected tile)
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

	def draw_textures(self,window):
		for i in self._pieces:
			i.draw(window,self.board_size)


	"""

	"""
	def init_board(self):
		pos = get_starting_pos(8)
		print(pos)
		for i in range(len(pos[0])):
			self._pieces.append(Piece(x=pos[0][i][0], y=pos[0][i][1], z=pos[0][i][2], color="white", texture=self._white, scale=self._scale))
			self._pieces.append(Piece(x=pos[1][i][0], y=pos[1][i][1], z=pos[1][i][2], color="black", texture=self._black, scale=self._scale))


	"""
		receive coords of a click on screen and takes action on it:
		- ignore coords out of bounds
		- translate screen coords to game coords (fcts.py screen_to_board(x,y))
		- on first click on a tile, hold coords
		- on second make move if legal
		- change self.player at the end of the turn(when a move is done)
	"""
	def click(self, screen_x, screen_y, screen_max_x, screen_max_y):
		if screen_x > screen_max_x or screen_y > screen_max_y:
			return
		game_coords = screen_to_board(screen_x, screen_y)
		if self._click == 0:
			self._click += 1
			try:
				self._hold = self._pieces[str(game_coords)]
			except KeyError:
				self._click = 0
				return
			self.list_moves()
			return
		if game_coords in self.valid_moves:
			self.move(game_coords[0], game_coords[1], game_coords[2])
			self._click = 0
			if self._player:
				self._player = 2
			else:
				self._player = 1


	"""
		list all coords the selected piece can move to
		!! keep promoted in mind !!
		!! keep 'infinite' board in mind !! (that's for later)
	"""
	def list_moves(self):
		x = self._hold.x
		y = self._hold.y
		z = self._hold.z
		if self._hold.promotion:
			pass #undefined for now
		else:
			all_moves = [(x, y + 2, z), (x, y - 2, z), (x - 2, y, z), (x, y, z + 2), (x, y, z - 2)]
			check_moves = self.has_pieces(all_moves)
			for m in all_moves:
				if not check_moves[all_moves.index(m)]:
					del all_moves[all_moves.index(m)]
			self.valid_moves = all_moves


	"""
		list all possible takes from selected piece to given coords
		!! only enemy !!
	"""
	def list_takes(self): #shows all possible takes for a piece for now, will be updated later to only give takes for selected move
		x = self._hold.x
		y = self._hold.y
		z = self._hold.z
		if self._hold.promotion:
			pass #undefined for now
		else:
			all_takes = [(x, y, z + 1), (x - 1, y, z + 1), (x, y + 1, z), (x - 1, y + 1, z), (x + 1, y - 1, z), (x + 1, y, z - 1)]
			check_enemy_present = self.has_pieces(all_takes)
			for t in all_takes:
				if not (check_enemy_present[all_takes.index(t)] and self._pieces[(x, y, z)].color != self._hold.color):
					del all_takes[all_takes.index(t)]
			self.valid_takes = all_takes


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
	def move(self, x, y, z):
		self._hold.move_piece(x, y, z)
