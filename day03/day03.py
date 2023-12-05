from utils.fileHelper import getLinesFor, writeListToFile
from utils.misc import Part
from typing import List

def inputToList(sample: bool = False) -> list[list[str]]:
    res = []
    lines = getLinesFor(day="03", sample=sample)
    for line in lines:
        res.append([*line.strip()])
    return res

def sumPartNumber(input: List[List[str]]) -> int:
    sum = 0
    for i in range(len(input)):
        curNumStr = ""
        curValid = False
        for j in range(len(input[0])):
            curChar = input[i][j]
            if curChar.isnumeric():
                curNumStr += curChar
                if not curValid:
                    curValid = curValid or isAdjacentToSymbol(input, i, j)
            else:
                if curNumStr and curValid:
                    sum += int(curNumStr)
                curNumStr = ""
                curValid = False
        if curNumStr and curValid:
            sum += int(curNumStr)
    return sum

def isAdjacentToSymbol(input: List[List[str]], i, j) -> bool:
    return isSymbol(input, i + 1, j) or \
            isSymbol(input, i - 1, j) or \
            isSymbol(input, i + 1, j + 1) or \
            isSymbol(input, i - 1, j - 1) or \
            isSymbol(input, i, j + 1) or \
            isSymbol(input, i, j - 1) or \
            isSymbol(input, i + 1, j - 1) or \
            isSymbol(input, i - 1, j + 1)             

def isSymbol(input: list[list[str]], x, y) -> bool:
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[x]):
        return False

    char = input[x][y]
    return not char == "." and not char.isnumeric()

def solve(part: Part):
    listInput = inputToList()
    res = sumPartNumber(listInput)
    print(res)


solve(Part.ONE)
