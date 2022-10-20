import pyglet
from pyglet import clock, font, image, window
from pyglet.window import key, Window

win = window.Window(fullscreen=True,caption="Checkers")
back = pyglet.sprite.Sprite(pyglet.resource.image("img/board.png"),0,0)
back.scale = win.get_size()[1] /back.height
print(back.height,win.get_size())

@win.event
def on_draw():
	win.clear()
	back.draw()

def update(delta_time):
	win.clear()
	back.draw()

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update,1/60)
	pyglet.app.run()