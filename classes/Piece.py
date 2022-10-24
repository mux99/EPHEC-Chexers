import pyglet

class Piece():
	"""
	class of a piece of ckeckers (on hexagonal tiled board)
	"""
	def __init__(self, x=0, y=0, z=0, color="White", texture=None, scale = 1):
		self._x = x
		self._y = y
		self._z = z
		self._color = color
		self._promotion = False

		self._sprite = pyglet.sprite.Sprite(texture,0,0)
		self._sprite.scale = scale


	"""
		promotion of piece to king
	"""
	def promote(self):
		self._promotion = True


	"""
		draw sprite of the piece
	"""
	def draw(self):
		self._sprite.draw()


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

	@x.setter
	def x(self, x):
		self._x = x

	@y.setter
	def y(self, y):
		self._y = y

	@z.setter
	def y(self, z):
		self._z = z
