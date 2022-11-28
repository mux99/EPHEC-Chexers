def read_csv(filename):
    """
        read a csv file and return matrix of string
        :filename: the string path to the file to be open

        :return: aray of arays of strings
    """
    out = []
    try:
        with open(filename, 'r') as file:
            for i in file.readlines():
                if i[0] != '#':
                    out.append(i.split(','))
    except OSError:
        print "Could not open/read file:", filename
    return out