import bin.fcts as fcts

from re import findall



class GameLogic:
	"""
		DO NOT USE ALONE
		extension of App class
	"""
	def is_piece(self, coord):
		"""
			receive coords (x,y,z),
			returns a boolean:
			True if a piece is in that place, False otherwise
		"""
		for piece in self._pieces:
			if coord == piece.coord:
				return True
		return False

	def get_piece(self, coord):
		"""
			return piece object at given coordonates, none if empty space
		"""
		for piece in self._pieces:
			if piece.coord == coord:
				return piece

	def take_piece(self, coord):
		"""
			take piece at given coords if any
		"""
		board = self._pieces
		for i in range(len(board)):
			if board[i].coord == coord:
				board[i].delete()
				del board[i]
				break

	def get_all_takes(self, coord, player):
		"""
			list takes for all possible moves
		"""
		out = []

		# list possible moves
		if self.get_piece(self._last_click).promotion:
			moves = self.get_moves_queen(coord, player)
		else:
			moves = self.get_moves(coord, player)

		# list takes for each moves
		for i in moves:
			out += self.get_takes(coord, i, player)
		return list(dict.fromkeys(out))

	def get_takes(self, coord, coord_2, player):
		"""
			list all takes for given moves
		"""
		out = []
		valid_takes = {(2, -1, -1): [(1, 0, -1), (1, -1, 0)],
							(1, -2, 1): [(1, -1, 0), (0, -1, 1)],
							(-1, -1, 2): [(0, -1, 1), (-1, 0, 1)],
							(-2, 1, 1): [(-1, 1, 0), (-1, 0, 1)],
							(-1, 2, -1): [(-1, 1, 0), (0, 1, -1)],
							(1, 1, -2): [(1, 0, -1), (0, 1, -1)]}

		move = fcts.vector_sub(coord_2, coord)
		# find parallel vector
		base_move = None
		for i in valid_takes.keys():
			if fcts.vector_cross_product(move, i) == (0, 0, 0) and fcts.is_the_right_parallel(move, i):
				base_move = i
				break
		# list takes
		tmp = coord
		while True:  # do while tmp2 != move
			if tmp == coord_2:
				break
			if base_move is None:
				break
			for i in valid_takes[base_move]:
				take_coord = fcts.vector_add(tmp, i)
				if self.is_piece(take_coord) and self.get_piece(take_coord).player == fcts.other_player(player):
					out.append(take_coord)
			tmp = fcts.vector_add(base_move, tmp)
		return out

	def get_moves(self, coord, player):
		"""
			return all coords of valid move from given coord
		"""
		out = []
		valid_moves = {"white": [(2, -1, -1), (1, -2, 1), (1, 1, -2)],
						"black": [(-2, 1, 1), (-1, 2, -1), (-1, -1, 2)]}
		valid_back_moves = {"white": [(-1, 2, -1), (-1, -1, 2)], "black": [(1, 1, -2), (1, -2, 1)]}

		# forward moves
		for i in valid_moves[player]:
			tmp = fcts.vector_add(coord, i)
			warp_coord = fcts.warp(tmp)
			if warp_coord is not None and not self.is_piece(warp_coord):
				out.append(warp_coord)
			if not self.is_piece(tmp) and fcts.validate_coords(tmp):
				out.append(tmp)

		# back takes
		for i in valid_back_moves[player]:
			tmp = fcts.vector_add(coord, i)
			if not self.is_piece(tmp) and fcts.validate_coords(tmp) and len(self.get_takes(coord, tmp, player)) != 0:
				out.append(tmp)

		return out

	def get_moves_queen(self, coord, player):
		"""
			return coords of valid moves form given coord for queen (promoted pieces)
		"""
		out = []
		valid_moves = [(2, -1, -1), (1, -2, 1), (1, 1, -2), (-1, 2, -1), (-2, 1, 1), (-1, -1, 2)]
		warp_coords = {}
		
		for i in valid_moves:
			tmp = fcts.vector_add(coord, i)
			warp_coord = fcts.warp(tmp)
			if warp_coord is not None and not self.is_piece(warp_coord):
				out.append(warp_coord)
				warp_coords[warp_coord] = i
			while not self.is_piece(tmp) and fcts.validate_coords(tmp):
				out.append(tmp)
				tmp = fcts.vector_add(tmp, i)
				warp_coord = fcts.warp(tmp)
				if warp_coord is not None and not self.is_piece(warp_coord):
					out.append(warp_coord)
					warp_coords[warp_coord] = i
		for w, m in warp_coords.items():
			tmp = fcts.vector_add(w, m)
			while not self.is_piece(tmp) and fcts.validate_coords(tmp):
				out.append(tmp)
				tmp = fcts.vector_add(tmp, m)

		return out

	
	def get_winner(self):
		"""
			returns which player wins
		"""
		black_pieces = [p for p in self._pieces if p.player == "black"]
		white_pieces = [p for p in self._pieces if p.player == "white"]
		return "white" if len(black_pieces) == 0 else "black"

	def game_is_finished(self):
		"""
			return True if a player wins, False if not
		"""
		string = self.__str__()  # this is not a good way to implement this but it looks cooler
		return len(findall("white", string)) == 0 or len(findall("black", string)) == 0
		# black_pieces = [p for p in self._pieces if p.player == "black"]
		# white_pieces = [p for p in self._pieces if p.player == "white"]
		# return len(black_pieces) == 0 or len(white_pieces) == 0
