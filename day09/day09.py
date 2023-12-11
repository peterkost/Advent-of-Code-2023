from typing import List
from utils.fileHelper import getLinesFor

PART = 2
SAMPLE = False

def estimateNextValueOf(line: str) -> int:
    values = extrapolateValuesOf(line)
    botVal = 0
    for i in range(len(values) - 1, -1, -1):
        botVal += values[i][-1]
    return botVal

def estimatePrevValueOf(line: str) -> int:
    values = extrapolateValuesOf(line)
    botVal = 0
    for i in range(len(values) - 1, -1, -1):
        botVal = values[i][0] - botVal 
    return botVal


def extrapolateValuesOf(line: str) -> List[List[int]]:
    nums = [int(n) for n in line.split()]
    history = [nums]
    while set(history[-1]) != set([0]):
        cur = []
        lastLine = history[-1]
        for i in range(0, len(lastLine) - 1):
            cur.append(lastLine[i + 1] - lastLine[i])
        history.append(cur)

    return history


def solve():
    lines = getLinesFor(day="09", sample=SAMPLE)
    res = sum([estimateNextValueOf(line) if PART == 1 else estimatePrevValueOf(line) for line in lines])
    print(res)


solve()
