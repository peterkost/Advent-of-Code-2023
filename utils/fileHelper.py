from typing import List


def getLinesFor(day: str, sample: bool = False) -> list[str]:
    input = open(f"inputs/day{day}{'-sample' if sample else ''}.txt", "r")
    return [line.strip() for line in input.readlines()]

def getInputAs2dList(day: str, sample: bool = False) -> List[List[str]]:
    lines = getLinesFor(day, sample)
    return [list(line) for line in lines]

def writeListToFile(input: list, name: str):
    file = open(f"tmp/{name}.txt", "w")
    for e in input:
        file.write("".join(e) + "\n")
    file.close()
