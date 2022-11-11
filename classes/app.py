import bin.fcts as fcts
from classes.piece import Piece
import re

from random import randint
import pyglet

class App():
	"""
		---TBD---
	"""
	def __init__(self):
		self._current_player = "white"

		#pieces
		self._pieces = [] #list all pieces on the board
		self._ghost_pieces = [] #pieces representing potential moves

		#coords
		self._clicked_coord = None
		self._possible_takes = []
		self._possible_moves = []

		#textures
		self.textures = {"black":None,"white":None}
		self._scale = 1
		self._select_opacity = 180

		#scaling
		self._tile_height = 1


	def __str__(self):
		return f"player:{self._current_player}\nboard:{self._pieces}"


	"""
		recalculate and update all scaling of pieces and distances
	"""
	def rescale(self,height):
		self._tile_height = height / 6.25
		self._scale = height / 2600
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
			self._pieces.append(Piece(coord=pos[0][i], player="white", texture=self.textures["white"],
				texture2=self.textures["white_queen"] ,scale=self._scale))
			self._pieces.append(Piece(coord=pos[1][i], player="black", texture=self.textures["black"],
				texture2=self.textures["black_queen"], scale=self._scale))

	"""
		change the piece selected based on games state and click coordonates
	"""
	def select(self, click_coords):
		if self.is_piece(click_coords) and self.get_piece(click_coords).player == self._current_player:
			if self._clicked_coord != None:
				self.get_piece(self._clicked_coord).opacity = 255
				#remove previous takes
				for i in self._possible_takes:
					self.get_piece(i).opacity = 255

			self._clicked_coord = click_coords
			self.get_piece(self._clicked_coord).opacity = self._select_opacity

			self._possible_moves = self.get_moves(self._clicked_coord,self._current_player)


	"""
	"""
	def move(self, click_coords):
		if not self.is_piece(click_coords) and self._clicked_coord != None:
			#only if move is valid
			if click_coords in self._possible_moves:
				#remove taken pieces
				for i in self.get_takes(self._clicked_coord,click_coords,self._current_player):
					self.take_piece(i)

				#move player
				self.get_piece(self._clicked_coord).coord = click_coords
				self.get_piece(click_coords).opacity = 255
				self._clicked_coord = None		


	"""
	"""
	def update(self, click_coords):
		#remove previous takes
		for i in self._possible_takes:
			try:
				self.get_piece(i).opacity = 255
			except AttributeError:
				#the piece dosn't exist anymore (killed)
				pass

		#update gamestate
		self._ghost_pieces = []
		if self._clicked_coord != None:
			#generate ghost pieces
			for i in self._possible_moves:
				tmp = Piece(texture=self.textures[self._current_player],scale=self._scale)
				tmp.coord = i
				tmp.opacity = 150
				self._ghost_pieces.append(tmp)

			#mark new takes
			self._possible_takes = self.get_all_takes(self._clicked_coord,self._current_player)
			for i in self._possible_takes:
				self.get_piece(i).opacity = 200

		if self._clicked_coord == None:
			self._possible_takes = []


	"""
		promote all pieces coresponding to criteria
	"""
	def promotion(self):
		for i in self._pieces:
			if not i.promotion and i.player == "white":
				if i.coord[0] == 7:
					i.promote()
			elif not i.promotion and i.player == "black":
				if i.coord[0] == 0:
					i.promote()


	"""
		receive coords of a click on screen and takes action on it based on curent game state
	"""
	def click(self, screen_x, screen_y):
		click_coords = fcts.screen_to_board(screen_x,screen_y,self._tile_height)

		#discard invalid clicks
		if not fcts.validate_click(click_coords):
			return

		self.select(click_coords)
		self.move(click_coords)
		self.update(click_coords)
		self.promotion()

		#AT temporary
		if self._clicked_coord == None:
			self.AI_move()
		
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
	"""
	def take_piece(self,coord):
		for i in range(len(self._pieces)):
			if self._pieces[i].coord == coord:
				self._pieces[i].delete()
				del self._pieces[i]
				break


	"""
		list takes for all possible moves
	"""
	def get_all_takes(self,coord,player):
		out = []
		for i in self.get_moves(coord,player):
			out += self.get_takes(coord,i,player)
		return list(dict.fromkeys(out))


	"""
		list all takes for given moves
	"""
	def get_takes(self,coord,coord_2,player):
		out = []
		valid_takes = {(2,-1,-1):[(1,0,-1),(1,-1,0)],
						(1,-2,1):[(1,-1,0),(0,-1,1)],
						(-1,-1,2):[(0,-1,1),(-1,0,1)],
						(-2,1,1):[(-1,0,1),(-1,1,0)],
						(-1,2,-1):[(-1,1,0),(0,1,-1)],
						(1,1,-2):[(0,1,-1),(1,0,-1)]}

		for i in valid_takes[fcts.vector_sub(coord_2,coord)]:
			tmp = fcts.vector_add(coord,i)
			if self.is_piece(tmp) and self.get_piece(tmp).player == fcts.other_player(player):
				out.append(tmp)
		return out


	"""
		return all coords of valid move from given coord
	"""
	def get_moves(self,coord,player):
		out = []
		valid_moves = {"white":[(2,-1,-1),(1,-2,1),(1,1,-2)],
						"black":[(-2,1,1),(-1,2,-1),(-1,-1,2)]}

		#forward moves
		for i in valid_moves[player]:
			tmp = fcts.vector_add(coord,i)
			if not self.is_piece(tmp) and fcts.validate_click(tmp):
				out.append(tmp)

		return out


	"""
		temporary-- to be replaced by multiplayer turns
	"""
	def AI_move(self):
		moves = []

		#list all possible moves
		for i in self._pieces:
			if i.player == "black":
				for j in self.get_moves(i.coord,"black"):
					moves.append((i.coord,j))

		#select a random move
		move = moves[randint(0,len(moves)-1)]
		if len(moves) > 0:
			for i in self.get_takes(move[0],move[1],"black"):
				self.take_piece(i)
			self.get_piece(move[0]).coord = move[1]

	def finish_game(self):
		string = self.__str__()
		if len(re.findall("white", string)) == 0 or len(re.findall("black", string)) == 0:
			return True
		return False

