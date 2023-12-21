from utils.fileHelper import getInputAs2dList
from utils.misc import Coords


GALAXY_SYMBOL = "#"


class Cosmos:
    def __init__(self, sampleInput: bool = False):
        m = getInputAs2dList(day="11", sample=sampleInput)
        rowLen, colLen = len(m), len(m[0])
        coords = []
        emptyRows, emptyCols = set([i for i in range(rowLen)]), set([j for j in range(colLen)])

        for x in range(rowLen):
            for y in range(colLen):
                if m[x][y] == GALAXY_SYMBOL:
                    emptyRows.discard(x)
                    emptyCols.discard(y)
                    coords.append(Coords(x,y))
        
        self.map, self.galaxyCoords, self.emptyRows, self.emptyCols = m, coords, emptyRows, emptyCols

