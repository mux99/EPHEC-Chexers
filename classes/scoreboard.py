from bin.file_intercation import read_csv

class Scoreboard():
    def __init__(self,filename):
        self.data = read_csv(filename)
    
    def sort(self):
        pass

    def add(self,name,score):
        pass