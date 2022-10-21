import pyglet
from pyglet import clock, font, image, window
from pyglet.window import key, Window

win = window.Window(fullscreen=True,caption="Checkers")
back = pyglet.sprite.Sprite(pyglet.resource.image("img/board.png"),0,0)

white = pyglet.sprite.Sprite(pyglet.resource.image("img/white.png"),0,0)

scale = win.get_size()[1] / back.height
print(scale)
back.scale = scale
white.scale = scale - 0.25

@win.event
def on_draw():
	win.clear()
	back.draw()

	white.draw() #temprary

def update(delta_time):
	pass

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update,1/60)
	pyglet.app.run()