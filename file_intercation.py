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
        print("Could not open/read file:", filename)
    return out


def scoreboard_add(*lines):
    """
        adds players scores to the scoreboard
    """
    for line in lines:
        if line is None or line.count(",") != 2:  # checks the format of the csv line to add
            return
        try:
            with open("scoreboard.csv", "a") as score_csv:
                score_csv.write(line)
                score_csv.close()
        except IOError:
            return