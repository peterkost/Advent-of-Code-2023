from utils.fileHelper import getInputAs2dList
from utils.misc import Coords


GALAXY_SYMBOL = "#"


class Cosmos:
    def __init__(self, sampleInput: bool = False):
        map = getInputAs2dList(day="11", sample=sampleInput)
        coords = []
        
        rowLen, colLen = len(map), len(map[0])
        emptyRows, emptyCols = set([i for i in range(rowLen)]), set([j for j in range(colLen)])
        for x in range(rowLen):
            for y in range(colLen):
                if map[x][y] == GALAXY_SYMBOL:
                    coords.append(Coords(x,y))
                    emptyRows.discard(x)
                    emptyCols.discard(y)
        
        self.map, self.galaxyCoords, self.emptyX, self.emptyY = map, coords, emptyRows, emptyCols

    def getNumEmptyBetween(self, a: Coords, b: Coords) -> int:
        numSpaces = 0

        smallerX, largerX = min(a.x, b.x), max(a.x, b.x)
        for x in range(smallerX + 1, largerX):
            if x in self.emptyX:
                numSpaces += 1
        
        smallerY, largerY = min(a.y, b.y), max(a.y, b.y)
        for y in range(smallerY + 1, largerY):
            if y in self.emptyY:
                numSpaces += 1

        return numSpaces

