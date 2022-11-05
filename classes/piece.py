import pyglet
from bin.fcts import screen_to_board, board_to_screen

class Piece():
	"""
	class of a piece of checkers (on hexagonal tiled board)
	"""
	def __init__(self, x=0, y=0, z=0, color="White", texture=None, scale = 1):
		self._x = x
		self._y = y
		self._z = z
		self._coord = (self._x, self._y, self._z)
		self._color = color
		self._promotion = False

		self._sprite = pyglet.sprite.Sprite(texture,0,0)

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
	def color(self):
		return self._color

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def z(self):
		return self._z

	@property
	def scale(self):
		return self._sprite.scale

	@property
	def texture(self):
		return self._sprite.texture

	@x.setter
	def x(self, x):
		self._x = x

	@y.setter
	def y(self, y):
		self._y = y

	@z.setter
	def z(self, z):
		self._z = z

	@scale.setter
	def scale(self, scale):
		self._sprite.scale = scale

	@texture.setter
	def texture(self, texture):
		self._sprite.texture = texture

