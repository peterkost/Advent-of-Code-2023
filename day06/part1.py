from typing import List, Tuple
from utils.fileHelper import getLinesFor

# (time, distance)
def parseInput(input: List[str]) -> List[Tuple[int, int]]:
    splitLines = []
    for line in input:
        elements = line.split()
        splitLines.append(elements[1:])
    res = []
    for i in range(len(splitLines[0])):
        res.append((int(splitLines[0][i]), int(splitLines[1][i])))
    return res

def getMinHoldTime(time: int, distance: int) -> int:
    l, r = 0, time
    res = time
    while l <= r:
        m = (l + r) // 2
        if isWinningHoldTime(time, m, distance):
            res = min(res, m)
            r = m - 1
        else:
            l = m + 1
    return res

def getMaxHoldTime(time: int, distance: int) -> int:
    l, r = 0, time
    res = 0
    while l <= r:
        m = (l + r) // 2
        if isWinningHoldTime(time, m, distance):
            res = max(res, m)
            l = m + 1
        else:
            r = m - 1
    return res

def isWinningHoldTime(time: int, holdTime: int, recordDistance: int) -> int:
    distanceTraveled = holdTime * (time - holdTime)
    return distanceTraveled > recordDistance

def solveDay06Part1():
    lines = getLinesFor("06", sample=False)
    races = parseInput(lines)
    res = 1
    for race in races:
        res *= getMaxHoldTime(race[0], race[1]) - getMinHoldTime(race[0], race[1]) + 1
    print(res)

solveDay06Part1()
