from math import sqrt
"""
translate the coord on screen to x,y,z hexagonal axis
"""
def screen_to_board(x, y, window):
	tile_height = window.height / 6.25
	board_x = (y - (tile_height * 0.5)) / (tile_height * 0.75)
	board_y = -((x + (board_x % 2 * tile_height * sqrt(0.1875) - (tile_height * 4 * sqrt(0.1875)))) / ((tile_height / 8) * (sqrt(3) / 2))) + ((y - (tile_height * 0.5)) / (tile_height * 0.375))
	board_z = -(board_x + board_y)
	return (int(board_x), int(board_y), int(board_z))


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x, y, z, window):
	return (z-y-(x%2)+4,(3*x)+2)

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