from bin.file_intercation import read_csv

class Scoreboard():
    def __init__(self,filename):
        self.data = read_csv(filename)
    
    def sort(self):
        pass

    def add(self,name,score):
        pass
    scoreboard_img = pyglet.resource.image("img/scoreboard.png")
	scoreboard_img.anchor_x = scoreboard_img.width//2
	scoreboard_img.anchor_y = scoreboard_img.height//2

    scoreboard_back = pyglet.sprite.Sprite(scoreboard_img, win.get_size()[0]//2, win.get_size()[1]//2)
    scoreboard_back.scale = scale/2.1