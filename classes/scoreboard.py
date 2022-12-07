import pyglet

from bin.file_intercation import read_csv

txt_h = 19.6
font_h = 35
name_max = 5
class Scoreboard():
	"""
		scoreboard of the game, to be displayed only when nesesary
	"""
	def __init__(self, filename:str, img, win):
		"""
		:filename: a valid file path
		:img: pyglet image of the background
		:win: the pyglet window to display on
		"""
		self._stack = []
		self.delay = 0
		self._file = filename
		self._data = list(read_csv(filename))[:10]
		self._sprite = pyglet.sprite.Sprite(img, 0, 0)
		self._names = [None for _ in range(len(self._data))]
		self._scores = [None for _ in range(len(self._data))]
		self._height = 0
		self._win = win

	def add(self, score:float, player:str):
		"""
		:score: a number
		:player: 'white' or 'black' is the current player
		"""
		self._stack.append(["",player,str(score)])
		if len(self._stack) == 1:
			self._data.append(self._stack[0])
			self._names.append(None)
			self._scores.append(None)
			self.rescale(self._height)

	def draw(self):
		""" draw all textures on screen
		"""
		self._sprite.draw()
		for i in self._names:
			if i != None:
				i.draw()
		for i in self._scores:
			if i != None:
				i.draw()

	def rescale(self, height):
		""" recalculate and update all scaling of textures and distances

		:height: the new height of the window in pixels
		"""
		self._height = height
		self._sprite.scale = (height/self._sprite.image.height)*0.8
		self._sprite.x = self._win.get_size()[0]//2
		self._sprite.y = self._win.get_size()[1]//2
		self._names = []
		self._scores = []
		for i in range(len(self._data)):
			if i >= 11:
				break
			self._names.append(pyglet.text.Label(self._data[i][0],font_size=height/font_h,font_name='Montserrat Alternates',anchor_y='center',color=(0,0,0,255)))
			self._names[i].x = self._sprite.x-(self._sprite.width/2.15)
			self._names[i].y = self._sprite.y+((height/txt_h)*(3-i))
			
			self._scores.append(pyglet.text.Label(self._data[i][2],font_size=height/font_h,font_name='Montserrat Alternates',anchor_y='center',color=(0,0,0,255)))
			self._scores[i].x = self._sprite.x-(self._sprite.width/6.25)
			self._scores[i].y = self._sprite.y+((height/txt_h)*(3-i))
	
	def keypress(self,key:str):
		""" call to write a name

		:key: the character of the pressed key 
		"""
		if len(self._data[-1][0]) < name_max and len(self._stack) > 0:
			self._data[-1][0] += key
			self._names[-1].text += key

	def backspace(self):
		""" call when backspace key is hit
		"""
		self._data[-1][0] = self._data[-1][0][:-1]
		self._names[-1].text = self._names[-1].text[:-1]
	
	def enter(self):
		""" call when enter key is hit
		"""
		if len(self._stack) == 0:
			return
		self.sort()
		i = 0
		tmp = []
		while i < len(self._data):
			if i == 0:
				i += 1
				continue
			if self._data[i][0] in tmp:
				del self._data[i]
			else:
				tmp.append(self._data[i][0])
				i += 1
		self.save()
		del self._stack[0]

		if len(self._stack) > 0:
			self._data.append(self._stack[0])
		self.rescale(self._height)

	def save(self):
		""" save curent state of scoreboard to file
		"""
		with open(self._file,'w') as file:
			file.write("\n".join([",".join(x) for x in self._data]))
	
	def sort(self):
		""" sort the scoreboard
		"""
		self._data = sorted(self._data, key=lambda i : -float(i[2]))
		self.rescale(self._height)
		