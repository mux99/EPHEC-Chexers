class Sprite:
    """
        sprite of the checkers pieces
    """
    def __init__(self, model = "img/black.png", x = 0, y = 0, z = 0):
        self._model = model
        self._x = x
        self._y = y
        self._z = z

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
    def z(self, z):
        self._z = z

    """
        move a sprite to screen coords
    """
    def move_sprite(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z