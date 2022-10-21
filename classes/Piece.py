class Piece(object):
	"""
	class of a piece of ckeckers (on hexagonal tiled board)
	"""
	def __init__(self, x=0, y=0, z=0, color=True):
		self._x = x
		self._y = y
		self._z = z
		self._color = color
		self._promotion = False

		self.texture #wil store the sprite of the piece to be displayed

	"""
	promotion of piece to king
	"""
	def promote(self):
		self._promotion = True

	@property
	def promotion(self):
		return self._promotion

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
