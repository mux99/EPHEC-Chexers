import pyglet
from pyglet import clock, font, image, window
from pyglet.window import key, Window

from classes.app import App

win = window.Window(resizable=True,caption="Checkers")
app = App()


@win.event
def on_draw():
	win.clear()

	back.draw()
	app.draw_textures(win)


@win.event
def on_resize(width, height):
	back.scale = height / back_img.height
	app.rescale(height / 2000)

@win.event
def on_mouse_press(x, y, button, modifiers):
     pass


"""
called once per game tick
dt: is the delta time between calls (---TBD--- check unit)
"""
def update(dt):
	pass #not usefull for now but mandatory

# @win.event
# def on_mouse_release(x, y, button, modifiers):
#     pass

# @win.event
# def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
#     pass

if __name__ == '__main__':
	#add background
	back_img = pyglet.resource.image("img/pixel_perfect_board.png")
	back = pyglet.sprite.Sprite(back_img,0,0)
	scale = win.get_size()[1] / back_img.height
	back.scale = scale

	#load pieces textures
	white = pyglet.resource.image("img/white.png")
	black = pyglet.resource.image("img/black.png")
	white.anchor_x = white.width // 2
	white.anchor_y = white.height // 2
	black.anchor_x = black.width // 2
	black.anchor_y = black.height // 2

	#setup board
	app.set_textures(white, black, scale=scale*0.73)
	app.init_board()

	#launch pyglet app (!= app.py App)
	pyglet.clock.schedule_interval(update,1/60)
	pyglet.app.run()