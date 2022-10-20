class Piece(object):
	"""

	"""
	def __init__(self, x=0, y=0, color=True):
		self._x = x
		self._y = y
		self._color = color
		self._promotion = False

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

	@x.setter
	def x(self, x):
		self._x = x

	@y.setter
	def y(self, y):
		self._y = y
