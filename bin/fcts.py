from math import sqrt
"""
translate the coord on screen to x,y,z hexagonal axis
"""
def screen_to_board(x, y):
	return (0,0,0)


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x, y, z, window, board_size):
	tile_height = window.height / 6.25 #distance of two oposite points of tht hexagon

	out_x = ((z-y) * tile_height/4 * sqrt(3)) - (x%2 * tile_height * sqrt(0.1875)) + (tile_height * 4 *sqrt(0.1875))
	out_y = (x * tile_height * 0.75) + (tile_height * 0.5)
	return (int(out_x),int(out_y),int(tile_height))

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