"""
translate the coord on screen to x,y,z hexagonal axis
"""
def screen_to_board(x,y):
	return (0,0,0)


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x,y,z):
	return (0,0)

"""
generate a list of starting locations for each color
"""
def get_starting_pos(n):
	whites = []
	blacks = []

	for i in range(n):
		whites.append((0,-n,n))
		whites.append((1,-n,n))

		blacks.append((7,-n,n))
		blacks.append((6,-n,n))


	return (whites,blacks)