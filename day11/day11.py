from day11.Cosmos import Cosmos
from utils.misc import Coords

# part 1 = 2, part 2 = 1000000
EXPANSION_MULTIPLIER = 1000000


def getSumOfShortestPaths(cosmos: Cosmos) -> int:
    sum = 0
    coords, lenCoords = cosmos.galaxyCoords, len(cosmos.galaxyCoords)
    for i in range(lenCoords):
        for j in range(i + 1, lenCoords):
            emptySpaces = cosmos.getNumEmptyBetween(coords[i], coords[j])
            addedSteps = emptySpaces  * (EXPANSION_MULTIPLIER - 1)
            res = getDistanceBetween(coords[i], coords[j]) + addedSteps
            sum +=  res
    return sum


def getDistanceBetween(a: Coords, b: Coords) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def solve():
    cosmos = Cosmos(sampleInput = False)
    sum = getSumOfShortestPaths(cosmos)
    print(sum)


solve()
