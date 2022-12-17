# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#

from math import sqrt, ceil, pi

def screen_to_board(x:int, y:int, tile_height:float):
	""" translate the coord on screen to x,y,z hexagonal axis
	:x: the x value in pixel of the click position
	:y: the y value in pixel of the click position
	:tile_height: the height of a tile on the board in pixel
	"""
	x -= sqrt(3)*tile_height * 1.25
	y -= tile_height/2
	board_x = ((2*y)/3)/(tile_height/2)
	board_z = ((x*sqrt(3) - y)/3)/(tile_height/2)
	board_y = - board_x - board_z
	return (round(board_x), round(board_y), round(board_z))


def vector_add(a:tuple, b:tuple):
	""" add 2 3D vectors together
	"""
	return (a[0]+b[0], a[1]+b[1], a[2]+b[2])


def vector_sub(a:tuple, b:tuple):
	""" subtract 2 3D vectors together
	"""
	return (a[0]-b[0], a[1]-b[1], a[2]-b[2])


def vector_cross_product(a:tuple, b:tuple):
	""" find the cross product of 2 3D vectors
	"""
	return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def is_the_right_parallel(a:tuple, b:tuple):
	""" determines if a vector is the parallel we are looking for

	a and b must be of same length
	"""
	for i in range(len(a)):
		if a[i] < 0 < b[i] or b[i] < 0 < a[i]:
			return False
	return True  # if you can't prove it's False it's True


def other_player(player:str):
	"""
	:return: the opposite player
	"""
	if player == "black":
		return "white"
	elif player == "white":
		return "black"


def board_to_screen(x:int, y:int, tile_height:float):
	""" translate the coords of hex tiles to their screen coords

	:x, y: valid board coordonate (Z is not needed)
	:tile_height: the height of a tile on the board in pixel

	see readme.md for infos on the coordonates system
	"""
	screen_x = (-((sqrt(3)*y)+(sqrt(3)*x/2)) * tile_height/2) + (sqrt(3)*tile_height*1.25)
	screen_y = ((3/2) * x * tile_height/2) + (tile_height/2)
	return (round(screen_x), round(screen_y))


def get_starting_pos(player):
	""" generate a list of starting locations for given player

	:player: 'white' or 'black', corresponds the current player
	"""
	out = []

	for i in range(8):
		if player == "white":
			out.append((0, -i, i))
			out.append((1, -i, i-1))
		elif player == "black":
			out.append((6, -i-3, i-3))
			out.append((7, -i-3, i-4))

	return out


def test_get_starting_pos(player):
	""" made for testing/debugging purpose only

	:player: 'white' or 'black', corresponds the current player
	"""
	if player == "white":
		return [(4, -5, 1)]
	elif player == "black":
		return [(4, -4, 0), (4, -6, 2), (5, -5, 0), (5, -6, 1), (3, -4, 1), (3, -5, 2),
				(2, -6, 4), (5, -8, 3), (2, -2, 0), (3, -2, -1), (3, -7, 4), (6, -8, 2), (1, -3, 2),
				(1, -4, 3), (5, -3, -2), (6, -4, -2)]
	return []

def test2_get_starting_pos(player):
	""" made for testing/debugging purpose only

	:player: 'white' or 'black' is the current player
	"""
	if player == "white":
		return [(4, -5, 1)]
	elif player == "black":
		return [(5, -5, 0)]
	return []


def validate_coords(coords):
	""" True if the coordinate are valid, False if not

	:coords: (x,y,z) valid coordinates of the board

		usable tiles coords follow a pattern like that:
		if x = 0 -> y = -8 to 2
		if x = 1 | 2 -> y = -9 to 1
		if x = 3 | 4 -> y = -10 to 0
		if x = 5 | 6 -> y = -11 to -1
		if x = 7 -> y = -12 to -2
		z isn't relevant since it depends on the value of x and y at the same time
	"""
	x = coords[0]
	y = coords[1]
	z = coords[2]

	if (x + y + z) != 0:
		print("Illegal Coordinates")
		return False

	if x == 0:
		return -8 <= y <= 2
	elif x in (1, 2):
		return -9 <= y <= 1
	elif x in (3, 4):
		return -10 <= y <= 0
	elif x in (5, 6):
		return -11 <= y <= -1
	elif x == 7:
		return -12 <= y <= -2
	else:
		return False


def warp(coords):
	""" gives the coordinates of the tile they can warp to
		see readme.md for rules on teleportation
	:coords: (x,y,z) valid coordinates of the board

	:return: warped coordinates, None if cannot warp
	"""
	x = coords[0]
	y = coords[1]
	z = coords[2]

	if 1 <= x <= 7 and 2 >= y >= -1:
		return vector_add(coords, (0, -11, 11)) if validate_coords(vector_add(coords, (0, -11, 11))) else None
	elif 0 <= x <= 6 and -12 <= y <= -9:
		return vector_add(coords, (0, 11, -11)) if validate_coords(vector_add(coords, (0, 11, -11))) else None
	return None


def takes_score(pieces_taken: int):
	"""
		:pieces_taken: amount of pieces taken in the turn
		:return: bonus points awarded for taking pieces
	"""
	return 100 << (pieces_taken - 1)


def get_pieces_bonus(pieces_left: int, queens: int):
	"""
		:pieces_left: amount of pieces the winner has at the end of the game
		:queens: int, how many of these pieces are queens
		:return: bonus points awarded for the amount of pieces and queens left
	"""
	return 100 << (queens ^ pieces_left) if (queens ^ pieces_left) > queens else 100 << queens


def get_time_bonus(time_spent: float):
	"""
		:time_spent: amount of seconds taken to play that turn
		:return: bonus points awarded for playing quickly
	"""
	return ceil(time_spent ** pi) if time_spent <= 10 else ceil(pi * time_spent/2)
