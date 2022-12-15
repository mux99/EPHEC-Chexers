# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#

from time import time
import pyglet

import bin.fcts as fcts
from classes.piece import Piece
from classes.game_logic import GameLogic
from classes.scoreboard import Scoreboard

class App(GameLogic):
	"""
		main app of the game
	"""
	def __init__(self,textures:dict,scoreboard:Scoreboard=None):
		""" constructor of app

		:textures: contains all the textures used for the game, as follows:
			'white' - normal piece
			'black' - normal piece
			'white_queen' - promoted piece
			'black_queen' - promoted piece
			'white_icon' - icon showing current player
			'black_icon' - icon showing current player
			'background' - the board

		:scoreboard: the scoreboard linked to the game (displayed and controlled separately)
		
		"""
		self._current_player = "white"
		self._continue = False
		self.player_names = {"white": None, "black": None}

		self._player_indicator = pyglet.sprite.Sprite(textures["white_icon"],0,0)
		self._background = pyglet.sprite.Sprite(textures["background"], 0, 0)

		self._scoreboard = scoreboard
		self._player_scores = {"white": 0, "black": 0}
		self.winner = None

		# pieces
		self._pieces = []
		self._ghost_pieces = []

		# coords
		self._last_click = None
		#self._last_click_time = 0
		self._possible_takes = []
		self._possible_moves = []

		# textures
		self.textures = textures
		self._select_opacity = 180

		# scaling
		self._tile_height = 1
		self.height = None

		# #fill board (testing positions)
		# for i in fcts.test2_get_starting_pos("white"):
		# 	self._pieces.append(Piece(i,"white",self.textures["white"],self.textures["white_queen"]))
		# for i in fcts.test2_get_starting_pos("black"):
		# 	self._pieces.append(Piece(i,"black",self.textures["black"],self.textures["black_queen"]))
		#fill board
		for i in fcts.get_starting_pos("white"):
			self._pieces.append(Piece(i,"white",self.textures["white"],self.textures["white_queen"]))
		for i in fcts.get_starting_pos("black"):
			self._pieces.append(Piece(i,"black",self.textures["black"],self.textures["black_queen"]))

	def __str__(self):
		return f"board:{self._pieces}"
	
	def preselect(self):
		pass

	def rescale(self, height:int):
		""" recalculate and update all scaling of textures and distances

		:height: the new height of the window in pixels
		"""
		self._background.scale = height/self._background.image.height
		self._tile_height = height / 6.25

		for i in self._pieces:
			i.scale = height / 2600

		for i in self._ghost_pieces:
			i.scale = height / 2600

		self._player_indicator.scale = height / 6500

	def draw_textures(self):
		""" draw all textures on screen

		depending on gamestate some textures will no be drawn
		"""
		self._background.draw()
		# draw pieces
		for i in self._pieces:
			i.draw(self._tile_height)

		# draw ghosts
		for i in self._ghost_pieces:
			i.draw(self._tile_height)
		
		if self.winner is None:
			self._player_indicator.draw()

	def select(self, new_click:tuple):
		"""change the piece selected based on games state and click coordinates

		:new_click: should contain x,y and z coordinates of the clicked tile
			see readme.md for info on the coordinate system

			do nothing if click on empty tile or the piece doesn't belong to the current player
		"""
		# click must be on a piece possessed by current player
		if not self.is_piece(new_click) or self.get_piece(new_click).player != self._current_player:
			return
		
		# player can only select a better or equal move
		if (len(self.get_all_takes(new_click,self._current_player)) < len(self._possible_takes) and self._last_click is not None):
			return

		# something was already selected
		if self._last_click is not None:
			self.get_piece(self._last_click).opacity = 255

		# select new piece
		self._last_click = new_click
		#self._last_click_time = time()
		self.get_piece(self._last_click).opacity = self._select_opacity

		# update possibe moves
		self._possible_moves = self.get_moves(self._last_click,self._current_player)

	def move(self, new_click:tuple):
		""" move selected piece to clicked location (if valid)

		:new_click: should contain x,y and z of the clicked tile
			see readme.md for info on the coordinate system

			do nothing if clicked tile isn't empty
		"""
		if self.is_piece(new_click) or self._last_click is None:
			return
		# only if move is valid
		found = None
		for i in self._possible_moves:
			if fcts.warp(i) == new_click:
				found = i
				break
		if found is None:
			return
		
		# remove taken pieces
		taken_pieces = 0
		for i in self.get_takes(self._last_click, found, self._current_player):
			taken_pieces += 1
			self.take_piece(fcts.warp(i))
		if taken_pieces > 0:
			self._player_scores[self._current_player] += fcts.takes_score(taken_pieces)

		# move player
		self.get_piece(self._last_click).coord = new_click
		self.get_piece(new_click).opacity = 255
			
		# select same piece if a take can be done
		self._last_click = None
		if len(self.get_all_takes(new_click,self._current_player)) > 0 and taken_pieces > 0:
			self.select(new_click)
			self._continue = True
		else:
			self._current_player = fcts.other_player(self._current_player)
			self.select(self.get_preselection(self._current_player))
			self._player_indicator.image = self.textures[self._current_player+"_icon"]
			self._continue = False

	def update(self):
		""" update and refresh various parameters of the game
		"""
		# remove previous takes
		for i in self._possible_takes:
			try:
				self.get_piece(i).opacity = 255
			except AttributeError:
				# the piece doesn't exist anymore (killed)
				pass
		
		# update gamestate
		self._ghost_pieces = []
		if self._last_click is not None:
			# generate ghost pieces
			for i in self._possible_moves:
				tmp = Piece(texture=self.textures[self._current_player],scale=self._pieces[0].scale)
				tmp.coord = i
				tmp.opacity = 100
				self._ghost_pieces.append(tmp)

			# mark new takes
			self._possible_takes = self.get_all_takes(self._last_click,self._current_player)
			for i in self._possible_takes:
				self.get_piece(i).opacity = 200

		else:
			self._possible_takes = []

			
	def promotion(self):
		"""promote all pieces worthy
		
		a worthy piece is sitting on the last opposite (from where it started) row of the board
		"""
		for i in self._pieces:
			if not i.promotion and i.player == "white":
				if i.coord[0] == 7:
					i.promote()
			elif not i.promotion and i.player == "black":
				if i.coord[0] == 0:
					i.promote()

	def click(self, screen_x:int, screen_y:int):
		"""receive coords of a click on screen and takes action on it based on current game state

		:screen_x: the x value in pixel of the click position
		:screen_y: the y value in pixel of the click position

		will select or move a piece on the board based on previous click
		do nothing if clicked twice on same tile
			or click coordinates are not on the board
		"""
		new_click = fcts.screen_to_board(screen_x, screen_y, self._tile_height)
		# print("click: ",new_click)

		# discard invalid clicks
		if not fcts.validate_coords(new_click):
			return

		# discard click twice
		if self._last_click == new_click:
			return

		if not self._continue:
			self.select(new_click)
		self.move(new_click)
		self.promotion()
		self.update()

		if self.is_game_finished():
			self.end_game()

		#self._last_click_time = time() - self._last_click_time
		#self._player_scores[self._current_player] += fcts.get_time_bonus(self._last_click_time)

	def end_game(self):
		""" is called at the end of the game
		calculate the score of each player and add them to the scoreboard
		"""
		self.winner = self.get_winner()
		pieces_left = len(self._pieces)
		queens = 0
		for p in self._pieces:
			if p.promotion:
				queens += 1
		self._player_scores[self.winner] += fcts.get_pieces_bonus(pieces_left, queens)
		if self._player_scores[self.winner] < self._player_scores[fcts.other_player(self.winner)]:
			# if the winner has a lower score than the loser, swap them
			tmp_high = self._player_scores[fcts.other_player(self.winner)]
			tmp_low = self._player_scores[self.winner]
			self._player_scores[fcts.other_player(self.winner)] = tmp_low
			self._player_scores[self.winner] = tmp_high
		if self._player_scores["white"].bit_length() > 21:  # if either player's score has more than 21 bits, truncate
			binary_white = bin(self._player_scores["white"])[:21]
			self._player_scores["white"] = int(binary_white, 2)
		if self._player_scores["black"].bit_length() > 21:
			binary_black = bin(self._player_scores["black"])[:21]
			self._player_scores["black"] = int(binary_black, 2)
		self._player_scores[fcts.other_player(self.winner)] *= 0.55  # winner's bonus but reversed
		self._player_scores[fcts.other_player(self.winner)] = \
		round(self._player_scores[fcts.other_player(self.winner)], 2)  # avoids floats with lots of 0s

		# add values to scoreboard 
		self._scoreboard.add(self._player_scores[self.winner],self.winner)
		self._scoreboard.add(self._player_scores[fcts.other_player(self.winner)],fcts.other_player(self.winner))
