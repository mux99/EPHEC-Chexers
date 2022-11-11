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
	add 2 3D vectors together
"""
def vector_add(vector1, vector2):
	return (vector1[0]+vector2[0],vector1[1]+vector2[1],vector1[2]+vector2[2])


"""
	add 2 3D vectors together
"""
def vector_sub(vector1, vector2):
	return (vector1[0]-vector2[0],vector1[1]-vector2[1],vector1[2]-vector2[2])


"""
	return the oposite player
"""
def other_player(player):
	if player == "black":
		return "white"
	elif player == "white":
		return "black"


"""
translate the coords of hex tiles to their screen coords
"""
def board_to_screen(x, y, z, tile_height):
	screen_x = (-((sqrt(3)*y)+(sqrt(3)*x/2)) * tile_height/2) + (2*sqrt(3)*tile_height/2)
	screen_y = ((3/2) * x * tile_height/2) + (tile_height/2)
	return (screen_x,screen_y)


"""
generate a list of starting locations for each player
"""
def get_starting_pos(n):
	whites = []
	blacks = []

	for i in range(n):
		whites.append((0,-i,i))
		whites.append((1,-i,i-1))

		blacks.append((6,-i-3,i-3))
		blacks.append((7,-i-3,i-4))

	return (whites,blacks)


"""
	return True if the coordinate are valid, False if not
	usable tiles coords follow a pattern like that:
	if x = 0 | 1 -> y = 0 to -7
	if x = 2 | 3 -> y = -1 to -8
	if x = 4 | 5 -> y = -2 to -9
	if x = 6 | 7 -> y = -3 to -10
	z isn't relevant since it depends on the value of x and y at the same time
	can't really check that without a big match statement with hardcoded values or lots of ifs :/
	works at least i guess ¯\_(ツ)_/¯ 
"""
def validate_click(coords):
	x = coords[0]
	y = coords[1]
	z = coords[2]

	if (x + y + z) != 0:
		print("Illegal Coordinates")
		return False

	if x in (0,1):
		return -7 <= y <= 0
	elif x in (2,3):
		return -8 <= y <= -1
	elif x in (4,5):
		return -9 <= y <= -2
	elif x in (6,7):
		return -10 <= y <= -3
	else:
		return False

"""
if the parameter is the coordinates of a teleportation tile return the coordinates of the destination
else return the parameter
"""
def teleport(cords):
    left = [(0,1,-1),(1,1,-2),(2,0,-2),(3,0,-3),(4,-1,-3),(5,-1,-4),(6,-2,-4),(7,-2,-5)]
    right = [(0,-8,8),(1,-8,7),(2,-9,7),(3,-9,6),(4,-10,6),(5,-10,5),(6,-11,5),(7,-11,4)]
    if cords in left:
        return (cords[0],cords[1]-8,cords[2]+8)
    elif cords in right:
        return (cords[0],cords[1]+8,cords[2]-8)
    else:
        return cords