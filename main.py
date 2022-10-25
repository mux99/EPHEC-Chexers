import pyglet
from pyglet import clock, font, image, window
from pyglet.window import key, Window

from classes.app import App

win = window.Window(resizable=True,caption="Checkers")
app = App()


@win.event
def on_draw():
	win.clear()

	#adjust background scale
	scale = win.get_size()[1] / back_base_height
	back.scale = scale


	back.draw()
	app.draw_textures()


"""
called once per game tick
dt: is the delta time between calls (---TBD--- check unit)
"""
def update(dt):
	pass #noy usefull for now


#----TYPE of mouse move to be determined
# @win.event
# def on_mouse_press(x, y, button, modifiers):
#     pass

# @win.event
# def on_mouse_release(x, y, button, modifiers):
#     pass

# @win.event
# def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
#     pass

if __name__ == '__main__':
	#add background
	back = pyglet.sprite.Sprite(pyglet.resource.image("img/board.png"),0,0)
	back_base_height = back.height
	scale = win.get_size()[1] / back_base_height
	back.scale = scale

	#load pieces textures
	white = pyglet.resource.image("img/white.png")
	black = pyglet.resource.image("img/black.png")

	#setup board
	app.set_textures(white, black, scale=scale*0.73)
	app.init_board()

	#launch pyglet app (!= app.py App)
	pyglet.clock.schedule_interval(update,1/60)
	pyglet.app.run()