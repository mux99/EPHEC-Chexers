import bin.fcts as fcts

"""
	DO NOT USE ALONE
	extention of App class
"""
class GameLogic():
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
		take piece at given coords if any
	"""
	def take_piece(self,coord):
		board = self._pieces
		for i in range(len(board)):
			if board[i].coord == coord:
				board[i].delete()
				del board[i]
				break


	"""
		list takes for all possible moves
	"""
	def get_all_takes(self,coord,player):
		out = []

		#list possible moves
		if self.get_piece(self._last_click).promotion:
			moves = self.get_moves_queen(coord,player)
		else:
			moves = self.get_moves(coord,player)

		#list takes for each moves
		for i in moves:
			out += self.get_takes(coord,i,player)
		return list(dict.fromkeys(out))


	"""
		list all takes for given moves
	"""
	def get_takes(self,coord,coord_2,player):
		out = []
		valid_takes = {(2,-1,-1):[(-1,0,1),(-1,1,0)],
						(1,-2,1):[(-1,1,0),(0,1,-1)],
						(-1,-1,2):[(0,1,-1),(1,0,-1)],
						(-2,1,1):[(1,0,-1),(1,-1,0)],
						(-1,2,-1):[(1,-1,0),(0,-1,1)],
						(1,1,-2):[(0,-1,1),(-1,0,1)]}

		move = fcts.vector_sub(coord_2,coord)

		#fix for longer move vectors
		if not move in valid_takes.keys():
			#find paralel vector
			for i in valid_takes.keys():
				if fcts.vector_cross_product(move,i) == (0,0,0):
					move = i
					break

		#list takes
		for i in valid_takes[move]:
			tmp = fcts.vector_add(coord_2,i)
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
		valid_back_moves = {"white":[(-1,2,-1),(-1,-1,2)],"black":[(1,1,-2),(1,-2,1)]}

		#forward moves
		for i in valid_moves[player]:
			tmp = fcts.vector_add(coord,i)
			if not self.is_piece(tmp) and fcts.validate_coords(tmp):
				out.append(tmp)

		#back takes
		for i in valid_back_moves[player]:
			tmp = fcts.vector_add(coord,i)
			if not self.is_piece(tmp) and fcts.validate_coords(tmp) and len(self.get_takes(coord,tmp,player)) != 0:
				out.append(tmp)

		return out


	"""
		return coords of valid moves form given coord for queen (promoted pieces)
	"""
	def get_moves_queen(self,coord,player):
		out = []
		valid_moves = [(2,-1,-1),(1,-2,1),(1,1,-2),(-1,2,-1),(-2,1,1),(-1,-1,2)]
		
		for i in valid_moves:
			tmp = fcts.vector_add(coord,i)
			while not self.is_piece(tmp) and fcts.validate_coords(tmp):
				out.append(tmp)
				tmp = fcts.vector_add(tmp,i)

		return out