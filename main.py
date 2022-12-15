# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#

import pyglet
from pyglet.window import key
from pyglet import font

# 'local' imports
from classes.app import App
from classes.scoreboard import Scoreboard

# add and load custom font for scoreboard
#font.add_file('fonts/MontserratAlternates-SemiBold.ttf')
#action_man = font.load('Monserrat Alternates Semi Bold', 16)

# generate a new windw
win = pyglet.window.Window(resizable=True, caption="Checkers")

@win.event
def on_draw():
	""" is call on each frame (framerate unknown)
	/!\ DO NOT MODIFY PARAMETERS
	"""
	win.clear()
	app.draw_textures()

	if app.winner is not None:
		scoreboard.draw()

@win.event
def on_resize(width, height):
	""" is called when window change size
	/!\ DO NOT MODIFY PARAMETERS
	"""
	app.rescale(height)
	scoreboard.rescale(height)

@win.event
def on_mouse_press(x, y, button, modifiers):
	""" is call on any mouse key input
	/!\ DO NOT MODIFY PARAMETERS
	"""
	if app.winner is None:
		app.click(x, y)

@win.event
def on_key_press(symbol, modifiers):
	""" is called on any keyboard input
	/!\ DO NOT MODIFY PARAMETERS
	"""
	if app.winner != None:
		if symbol >= 33 and symbol <= 126:
			scoreboard.keypress(chr(symbol))
		elif symbol == key.BACKSPACE:
			scoreboard.backspace()
		elif symbol == key.ENTER:
			scoreboard.enter()

if __name__ == '__main__':
	# load textures to altas
	atlas = {"white": pyglet.resource.image("img/white.png"),
				"black": pyglet.resource.image("img/black.png"),
				"white_queen": pyglet.resource.image("img/white_queen.png"),
				"black_queen": pyglet.resource.image("img/black_queen.png"),
				"white_icon": pyglet.resource.image("img/white_icon.png"),
				"black_icon": pyglet.resource.image("img/black_icon.png"),
				"background": pyglet.resource.image("img/board.png"),
				"scoreboard": pyglet.resource.image("img/scoreboard.png")}

	# window icon
	win.set_icon(pyglet.resource.image("img/logo32.png"))

	# center textures on themselves (most of them anyway)
	for i in atlas.keys():
		if i not in ["white_icon","black_icon","background"]:
			atlas[i].anchor_x = atlas[i].width // 2
			atlas[i].anchor_y = atlas[i].height // 2

	# setup board
	scoreboard = Scoreboard("data/scoreboard.csv",atlas["scoreboard"],win)
	app = App(atlas,scoreboard)

	# launch window
	pyglet.app.run()
