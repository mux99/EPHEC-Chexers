from math import sqrt
"""
translate the coord on screen to x,y,z hexagonal axis
"""
def screen_to_board(x, y):
	board_x = (y - 2) / 3
	board_y = (-x - board_x - (board_x % 2) + 4) / 2
	board_z = -board_x - board_y
	return (board_x, board_y, board_z)


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x, y, z, tile_height):
	screen_x = (z-y - (x%2)+ 4) * tile_height * 0.433
	screen_y = ((3*x) + 2) * tile_height * 0.25
	return (screen_x,screen_y)

"""
generate a list of starting locations for each color
"""
def get_starting_pos(n):
	whites = []
	blacks = []

	for i in range(n):
		whites.append((0,-i,i))
		whites.append((1,-i,i))

		blacks.append((7,-i,i))
		blacks.append((6,-i,i))


	return (whites,blacks)