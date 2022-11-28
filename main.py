import pyglet
from pyglet import clock, font, image, window
from pyglet.window import key, Window
#from pyautogui import prompt
from classes.app import App


win = window.Window(resizable=True, caption="Checkers")
app = App()


@win.event
def on_draw():
	win.clear()
	back.draw()
	app.draw_textures()


@win.event
def on_resize(width, height):
	back.scale = height / back_img.height
	app.rescale(height)


@win.event
def on_mouse_press(x, y, button, modifiers):
	app.click(x, y)
	# app.AI_move()


def update(dt):
	"""
	called once per game tick
	dt: is the delta time between calls (---TBD--- check unit, ms?)
	"""
	pass  # not useful for now but mandatory


if __name__ == '__main__':
	# add background
	back_img = pyglet.resource.image("img/board.png")
	back = pyglet.sprite.Sprite(back_img, 0, 0)
	scale = win.get_size()[1] / back_img.height
	back.scale = scale

	# load pieces textures
	textures = {"white": pyglet.resource.image("img/white.png"),
				"black": pyglet.resource.image("img/black.png"),
				"white_queen": pyglet.resource.image("img/white_queen.png"),
				"black_queen": pyglet.resource.image("img/black_queen.png"),
				"white_icon": pyglet.resource.image("img/white_icon.png"),
				"black_icon": pyglet.resource.image("img/black_icon.png")}

	# center texture pivot
	for i in textures.keys():
		if i != "white_icon" and i!= "black_icon":
			textures[i].anchor_x = textures[i].width // 2
			textures[i].anchor_y = textures[i].height // 2

	# setup board
	app.textures = textures
	app.scale = scale*0.73
	app.init_board()
	# player1_name = prompt("Enter a name for player 1: ", "Checkers")
	# player2_name = prompt("Enter a name for player 2: ", "Checkers")
	# while player1_name is None or len(player1_name) == 0:
	#	player1_name = prompt("Enter a name for player 1: ", "Checkers")
	# while player2_name is None or len(player2_name) == 0:
	#	player2_name = prompt("Enter a name for player 2: ", "Checkers")
	# app.player_names["white"] = player1_name
	# app.player_names["black"] = player2_name
	# launch pyglet app (!= app.py App)
	pyglet.clock.schedule_interval(update, 1/60)
	pyglet.app.run()
