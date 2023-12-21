from day11.Cosmos import Cosmos
from utils.misc import Coords


def getSumOfShortestPaths(cosmos: Cosmos) -> int:
    sum = 0
    coords, lenCoords = cosmos.galaxyCoords, len(cosmos.galaxyCoords)
    for i in range(lenCoords):
        for j in range(i + 1, lenCoords):
            sum += getDistanceBetween(coords[i], coords[j])
    return sum


def getDistanceBetween(a: Coords, b: Coords) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


def solve():
    cosmos = Cosmos(sampleInput = False)
    sum = getSumOfShortestPaths(cosmos)
    print(sum)


solve()
