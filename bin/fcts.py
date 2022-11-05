from math import sqrt

"""
translate the coord on screen to x,y,z hexagonal axis
"""
def screen_to_board(x, y, tile_height):
	x -= 2*sqrt(3)*tile_height/2
	y -= tile_height/2
	board_x = ((2*y)/3)/(tile_height/2)
	board_z = ((x*sqrt(3) - y)/3)/(tile_height/2)
	board_y = - board_x - board_z
	return (round(board_x), round(board_y), round(board_z))


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x, y, z, tile_height):
	screen_x = (-((sqrt(3)*y)+(sqrt(3)*x/2)) * tile_height/2) + (2*sqrt(3)*tile_height/2)
	screen_y = ((3/2) * x * tile_height/2) + (tile_height/2)
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

		blacks.append((6,-i-3,i+3))
		blacks.append((7,-i-3,i+3))


	return (whites,blacks)