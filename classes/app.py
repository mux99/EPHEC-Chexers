import bin.fcts as fcts
from classes.piece import Piece

import pyglet

class App():
	"""
		---TBD---
	"""
	def __init__(self):
		self._curent_player = "white"

		#pieces
		self._pieces = [] #list all pieces on the board
		self._ghost_pieces = [] #pieces representing potential moves

		#coords
		self._clicked_coord = None

		#textures
		self.textures = {}
		self._scale = 1
		self._select_opacity = 180

		#scaling
		self._tile_height = 1


	"""
		recalculate and update all scaling of pieces and distances
	"""
	def rescale(self,height):
		self._tile_height = height / 6.25
		self._scale = height / 2000
		for i in self._pieces:
			i.scale = self._scale

		for i in self._ghost_pieces:
			i.scale = self._scale


	"""
		draw all pieces on the board
	"""
	def draw_textures(self):
		#draw pieces
		for i in self._pieces:
			i.draw(self._tile_height)

		#draw ghosts
		for i in self._ghost_pieces:
			i.draw(self._tile_height)


	"""
		fill board with pieces at their correct starting positions
	"""
	def init_board(self):
		pos = fcts.get_starting_pos(8)
		for i in range(len(pos[0])):
			self._pieces.append(Piece(x=pos[0][i][0], y=pos[0][i][1], z=pos[0][i][2],
				color="white", texture=self.textures["white"], scale=self._scale))
			self._pieces.append(Piece(x=pos[1][i][0], y=pos[1][i][1], z=pos[1][i][2],
				color="black", texture=self.textures["black"], scale=self._scale))


	"""
		receive coords of a click on screen and takes action on it based on curent game state
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
		
		click_coords = fcts.screen_to_board(screen_x,screen_y,self._tile_height)

		#discard invalid clicks
		if not fcts.validate_click(click_coords):
			return

		#select piece
		if self.is_piece(click_coords) and self.get_piece(click_coords).color == self._curent_player:
			if self._clicked_coord != None:
				self.get_piece(self._clicked_coord).opacity = 255

			self._clicked_coord = click_coords
			self.get_piece(self._clicked_coord).opacity = self._select_opacity

		#move selected
		elif not self.is_piece(click_coords) and self._clicked_coord != None:
			#move only if move is valid
			if click_coords in self.get_moves(self._clicked_coord,self._curent_player):
				self.get_piece(self._clicked_coord).coord = click_coords
				self.get_piece(click_coords).opacity = 255
				self._clicked_coord = None

		#generate ghost pieces
		self._ghost_pieces = []
		if self._clicked_coord != None:
			for i in self.get_moves(self._clicked_coord,self._curent_player):
				tmp = Piece(texture=self.textures[self._curent_player],scale=self._scale)
				tmp.coord = i
				tmp.opacity = 150
				self._ghost_pieces.append(tmp)

		
	"""
		receive coords (x,y,z),
		returns a boolean:
		True if a piece is in that place, False otherwise
	"""
	def is_piece(self, coord):
		for piece in self._pieces:
			if coord == piece.coord:
				return True
		return False


	"""
		return piece object at given coordonates, none if empty space
	"""
	def get_piece(self,coord):
		for piece in self._pieces:
			if piece.coord == coord:
				return piece


	"""
		return all coords of valid move from given coord
	"""
	def get_moves(self,coord,color):
		out = []
		valid_moves = {"white":[(2,-1,-1),(1,-2,1),(1,1,-2)],
						"black":[(-2,1,1),(-1,2,-1),(-1,-1,2)]}

		#forward moves
		for i in valid_moves[color]:
			tmp = fcts.vector_add(i,coord)
			if not self.is_piece(tmp) and fcts.validate_click(tmp):
				out.append(tmp)

		return out

