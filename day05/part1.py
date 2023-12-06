from typing import List, Tuple
from utils.fileHelper import getLinesFor


def seedToLocation(seed: int, chain: List[List[Tuple[int, int, int]]]) -> int:
    cur = seed
    for map in chain:
        l, r = 0, len(map) - 1
        while l <= r:
            m = (r + l) // 2
            start, end, change = map[m]
            if start <= cur <= end:
                cur += change
                break
            if end < cur:
                l = m + 1
            else:
                r = m - 1
    return cur

def getSeeds(line: str) -> List[int]:
    strSeeds = line.replace("seeds: ", "").split()
    return [int(seed) for seed in strSeeds]

def getChainOfMaps(lines: List[str]) ->List[List[Tuple[int, int, int]]]:
    res = []
    processedInput = getInputMapsAsList(lines)

    for map in processedInput:
        formatedMap = []
        for e in map:
            asRange = convertInputToRange(e)
            formatedMap.append(asRange)
        res.append(sorted(formatedMap))

    return res

def getInputMapsAsList(lines: List[str]) -> List[List[int]]:
    res = []
    i = 0
    while i < len(lines):
        curMap = []

        while i < len(lines) and lines[i]:
            if lines[i][0].isnumeric():
                lineAsInt = [int(strNum) for strNum in lines[i].split()]
                curMap.append(lineAsInt)
            i += 1
        i += 1
        res.append(curMap)
    return res

def convertInputToRange(input: List[int]) -> Tuple[int, int, int]:
    destStart, sourceStart, rangeLen = input
    sourceEnd = sourceStart + rangeLen  - 1
    change =  destStart - sourceStart

    return (sourceStart, sourceEnd, change)


def getAndPrintAnswer():
    lines = getLinesFor(day="05", sample=True)

    seeds = getSeeds(lines[0])
    chainOfMaps = getChainOfMaps(lines[2:])
    locations = []

    for seed in seeds:
        locations.append(seedToLocation(seed, chainOfMaps))

    print(min(locations))

if __name__ == "__main__":
   getAndPrintAnswer()
