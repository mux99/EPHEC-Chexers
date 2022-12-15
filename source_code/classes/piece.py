# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#

import pyglet

from bin.fcts import board_to_screen, warp


class Piece:
	""" class of a piece of checkers (on hexagonal tiled board)
	"""

	def __init__(self, coord: tuple = (0, 0, 0), player: str = "White", texture=None, texture2=None, promotion=False, scale: float = 1):
		""" constructor of Piece
		:coords: (x,y,z) valid coordonates of the board, the piece's coordonates
		:player: 'white' or 'black', the player it belongs to
		:texture: the normal texture
		:texture2: the promoted texture
		:promotion: --debug purposes--
		:scale: scaling factor of the sprite
		"""
		self._coord = warp(coord)
		self._player = player
		self._promotion = promotion

		if texture is not None:
			self._sprite = pyglet.sprite.Sprite(texture, 0, 0)
			self._sprite.scale = scale
		if texture2 is not None:
			self._promotion_texture = texture2

	def __repr__(self):
		return str(self)

	def __str__(self):
		return f"{self._player}:{self._coord}"

	def promote(self):
		""" promotion of piece to queen
		"""
		print("promote")
		tmp = self._sprite.scale
		self._promotion = True
		self._sprite = pyglet.sprite.Sprite(self._promotion_texture, 0, 0)
		self._sprite.scale = tmp

	def draw(self, tile_height):
		""" draw sprite of the piece
		"""
		pos = board_to_screen(self._coord[0], self._coord[1], tile_height)
		self._sprite.x = pos[0]
		self._sprite.y = pos[1]
		self._sprite.draw()

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
	def scale(self):
		return self._sprite.scale

	@property
	def opacity(self):
		return self._sprite.opacity

	@coord.setter
	def coord(self, coord: tuple):
		"""
		:coord: (x,y,z) valid coordonates of the board, the piece's coordonates
		"""
		self._coord = warp(coord)

	@scale.setter
	def scale(self, scale: float):
		self._sprite.scale = scale

	@opacity.setter
	def opacity(self, opacity: int):
		"""
		:opacity: between 0 and 255
			255 is opaque, 0 is invisible
		"""
		self._sprite.opacity = opacity

	def delete(self):
		self._sprite.delete()
