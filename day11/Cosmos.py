from utils.fileHelper import getInputAs2dList
from utils.misc import Coords
from typing import List, Set


GALAXY_SYMBOL = "#"


class Cosmos:
    def __init__(self, sampleInput: bool = False):
        inputMap = getInputAs2dList(day="11", sample=sampleInput)
        coords = []

        inputRowLen, inputColLen = len(inputMap), len(inputMap[0])
        emptyRows, emptyCols = set([i for i in range(inputRowLen)]), set([j for j in range(inputColLen)])
        for x in range(inputRowLen):
            for y in range(inputColLen):
                if inputMap[x][y] == GALAXY_SYMBOL:
                    emptyRows.discard(x)
                    emptyCols.discard(y)

        expandedMap = Cosmos._expandMap(inputMap, emptyRows, emptyCols)
        expandedRowLen, expandedColLen = len(expandedMap), len(expandedMap[0])
        for x in range(expandedRowLen):
            for y in range(expandedColLen ):
                if expandedMap[x][y] == GALAXY_SYMBOL:
                    coords.append(Coords(x,y))
        
        self.map, self.galaxyCoords= expandedMap, coords

    @staticmethod
    def _expandMap(og: List[List[str]], row: Set[int], col: Set[int]) -> List[List[str]]:
        ex = og[:]
        for i in sorted(list(row), reverse=True):
            ex.insert(i,["."] * len(ex[0]))

        for j in sorted(list(col), reverse= True):
            for k in range(len(ex)):
                ex[k].insert(j, ".")
        return ex


