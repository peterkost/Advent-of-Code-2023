from typing import List, Tuple
from utils.fileHelper import getLinesFor
from day05.part1 import getChainOfMaps, getSeeds, seedToLocation
from tqdm import tqdm


# [(start, end)]
def getSeedRanges(input: str) -> List[Tuple[int, int]]:
    seeds = getSeeds(input)

    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))

    return ranges


def getAndPrintAnswer():
    lines = getLinesFor(day="05", sample=False)

    seedRanges = getSeedRanges(lines[0])
    chainOfMaps = getChainOfMaps(lines[2:])

    minLocation = float('inf')

    for r in tqdm(range(len(seedRanges))):
        s, e = seedRanges[r]
        for seed in tqdm(range(s, e)):
            minLocation = min(minLocation, seedToLocation(seed, chainOfMaps))

    print(minLocation)


if __name__ == "__main__":
   getAndPrintAnswer()
