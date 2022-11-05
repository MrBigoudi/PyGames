WALL = 1
NONE = 0
PLAYER = 2

class Map:
    def __init__(self, filePath):
        lines = open(filePath, "r").readlines()
        
        self.nbRaws = int(lines[0].replace(" ", "").replace("\n", "").split(':')[1])
        self.nbCols = int(lines[1].replace(" ", "").replace("\n", "").split(':')[1])
        # print(self.nbRaws, self.nbCols)
        self.map = []

        try:
            for i in range(2,self.nbRaws+2):
                raw = []
                for j in range(self.nbCols):
                    # print(lines[i][j])
                    raw.append(int(lines[i][j]))
                # print(raw)
                self.map.append(raw)
        except:
            raise Exception("Incorrect file format for " + filePath)