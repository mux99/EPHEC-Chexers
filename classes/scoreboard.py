import pyglet

from bin.file_intercation import read_csv

txt_h = 19.8
class Scoreboard():
	def __init__(self, filename, img, win):
		self.delay = 0
		self._file = filename
		self._data = list(read_csv(filename))[:10]
		self._sprite = pyglet.sprite.Sprite(img, 0, 0)
		self._names = [None for _ in range(len(self._data))]
		self._scores = [None for _ in range(len(self._data))]
		self._height = 0
		self._win = win

	def add(self, score, player):
		self._data.append(["",player,str(score)])
		self._names.append(None)
		self._scores.append(None)
		self.rescale(self._height)

	def draw(self):
			self._sprite.draw()
			for i in self._names:
				if i != None:
					i.draw()
			for i in self._scores:
				if i != None:
					i.draw()

	def rescale(self, height):
		self._height = height
		self._sprite.scale = (height/self._sprite.image.height)*0.8
		self._sprite.position = (self._win.get_size()[0]//2, self._win.get_size()[1]//2)
		self._names = []
		self._scores = []
		for i in range(len(self._data)):
			if i >= 10:
				break
			self._names[i] = pyglet.text.Label(self._data[i][0],font_size=height/28,anchor_y='center',color=(0,0,0,255))
			self._names[i].position = (self._sprite.position[0]-(self._sprite.width/2.1),self._sprite.position[1]+((height/txt_h)*(3-i)))
			
			self._scores[i] = pyglet.text.Label(self._data[i][2],font_size=height/28,anchor_y='center',color=(0,0,0,255))
			self._scores[i].position = (self._sprite.position[0]-(self._sprite.width/6.25),self._sprite.position[1]+((height/txt_h)*(3-i)))
	
	def keypress(self,key):
		if len(self._data[-1][0]) <= 4:
			self._data[-1][0] += key
			self._names[-1].text += key

	def backspace(self):
		self._data[-1][0] = self._data[-1][0][:-1]
		self._names[-1].text = self._names[-1].text[:-1]
	
	def enter(self):
		self.sort()
		self.save()

	def save(self):
		with open(self._file,'w') as file:
			file.write("\n".join([",".join(x) for x in self._data]))
	
	def sort(self):
		self._data = sorted(self._data, key=lambda i : -int(i[2]))
		self.rescale(self._height)
		