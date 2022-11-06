import pyglet
from bin.fcts import screen_to_board, board_to_screen

class Piece():
	"""
	class of a piece of checkers (on hexagonal tiled board)
	"""
	def __init__(self, coord=(0,0,0), player="White", texture=None, scale = 1):
		self._x = coord[0]
		self._y = coord[1]
		self._z = coord[2]
		self._player = player
		self._promotion = False

		self._sprite = pyglet.sprite.Sprite(texture,0,0)
		self._sprite.scale = scale

	def __repr__(self):
		return str(self)

	def __str__(self):
		return f"({self._x},{self._y},{self._z})"


	"""
		promotion of piece to king
	"""
	def promote(self):
		self._promotion = True


	"""
		draw sprite of the piece
	"""
	def draw(self,tile_height):
		pos = board_to_screen(self._x, self._y, self._z, tile_height)
		self._sprite.x = pos[0]
		self._sprite.y = pos[1]
		self._sprite.draw()
		

	"""
		change coords of the selected piece
	"""
	def move_piece(self, x, y, z):
		self._x = x
		self._y = y
		self._z = z
		self._coord = (x, y, z)


	@property
	def coord(self):
		return self._coord

	@property
	def promotion(self):
		return self._promotion

	@property
	def player(self):
		return self._player

	@property
	def coord(self):
		return (self._x,self._y,self._z)

	@property
	def scale(self):
		return self._sprite.scale

	@property
	def opacity(self):
		return self._sprite.opacity

	@property
	def color(self):
		return self._sprite.color

	@coord.setter
	def coord(self, coord):
		self._x = coord[0]
		self._y = coord[1]
		self._z = coord[2]

	@scale.setter
	def scale(self, scale):
		self._sprite.scale = scale

	@opacity.setter
	def opacity(self, opacity):
		self._sprite.opacity = opacity

	@color.setter
	def color(self, color):
		self._sprite.color = color



