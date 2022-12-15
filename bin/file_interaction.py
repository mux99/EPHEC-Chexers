# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#
import os


def read_csv(filename):
    """ read a csv file and return matrix of string
    
    :filename: the string path to the file to be open
    
    :return: tuple of tuples of strings
    """
    out = []
    try:
        with open(filename, 'r') as file:
            for i in file.readlines():
                if i[0] != '#':
                    out.append(tuple(i.strip().split(',')))
    except OSError:
        print("Could not open/read file:", filename)
    return tuple(out)


def is_file(path):
    if type(path) != str:
        raise TypeError
    return os.path.exists(path)

def create_file(path):
    if type(path) != str:
        raise TypeError
    if not is_file(path):
        with open(path, 'w'):
            pass
