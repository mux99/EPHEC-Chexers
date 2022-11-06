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
	app.draw_textures()

@win.event
def on_resize(width, height):
	back.scale = height / back_img.height
	app.rescale(height)

@win.event
def on_mouse_press(x, y, button, modifiers):
	app.click(x,y)


"""
called once per game tick
dt: is the delta time between calls (---TBD--- check unit, ms?)
"""
def update(dt):
	pass #not usefull for now but mandatory


if __name__ == '__main__':
	#add background
	back_img = pyglet.resource.image("img/pixel_perfect_board.png")
	back = pyglet.sprite.Sprite(back_img,0,0)
	scale = win.get_size()[1] / back_img.height
	back.scale = scale

	#load pieces textures
	textures = {"white":pyglet.resource.image("img/white.png"),"black":pyglet.resource.image("img/black.png")}

	#center texture pivot
	for i in textures.keys():
		textures[i].anchor_x = textures[i].width // 2
		textures[i].anchor_y = textures[i].height // 2

	#setup board
	app.textures = textures
	app.scale = scale*0.73
	app.init_board()

	#launch pyglet app (!= app.py App)
	pyglet.clock.schedule_interval(update,1/60)
	pyglet.app.run()