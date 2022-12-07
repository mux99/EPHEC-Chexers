import pyglet
from pyglet.window import key
from pyglet import font

font.add_file('fonts/MontserratAlternates-SemiBold.ttf')
action_man = font.load('Monserrat Alternates Semi Bold', 16)

#from pyautogui import prompt
from classes.app import App
from classes.scoreboard import Scoreboard


win = pyglet.window.Window(resizable=True, caption="Checkers")

@win.event
def on_draw():
	win.clear()
	app.draw_textures()

	if app.winner is not None:
		scoreboard.draw()

@win.event
def on_resize(width, height):
	app.rescale(height)
	scoreboard.rescale(height)

@win.event
def on_mouse_press(x, y, button, modifiers):
	if app.winner is None:
		app.click(x, y)

@win.event
def on_key_press(symbol, modifiers):
	if app.winner is not None:
		if 33 <= symbol <= 126:
			scoreboard.keypress(chr(symbol))
		elif symbol == key.BACKSPACE:
			scoreboard.backspace()
		elif symbol == key.ENTER:
			scoreboard.enter()

if __name__ == '__main__':
	# load pieces textures
	textures = {"white": pyglet.resource.image("img/white.png"),
				"black": pyglet.resource.image("img/black.png"),
				"white_queen": pyglet.resource.image("img/white_queen.png"),
				"black_queen": pyglet.resource.image("img/black_queen.png"),
				"white_icon": pyglet.resource.image("img/white_icon.png"),
				"black_icon": pyglet.resource.image("img/black_icon.png"),
				"background": pyglet.resource.image("img/board.png"),
				"scoreboard": pyglet.resource.image("img/scoreboard.png")}

	# center texture pivot
	for i in textures.keys():
		if i not in ["white_icon","black_icon","background"]:
			textures[i].anchor_x = textures[i].width // 2
			textures[i].anchor_y = textures[i].height // 2

	# setup board
	scoreboard = Scoreboard("data/scoreboard.csv",textures["scoreboard"],win)

	app = App(textures,scoreboard)

	pyglet.app.run()
