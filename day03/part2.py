from collections import defaultdict
from day03.part1 import inputToList
from typing import List, Dict, Tuple

def getGearMap(input: List[List[str]]) -> Dict:
    gearMap = defaultdict(list) # {(gearX, gearY):[adjacentNumber]}
    for i in range(len(input)):
        curNumStr = ""
        indiciesOfGearsTouchingCur = set()
        for j in range(len(input[0])):
            curChar = input[i][j]
            if curChar.isnumeric():
                curNumStr += curChar
                isAdjacentToGear(input, i, j, indiciesOfGearsTouchingCur)
            else:
                if curNumStr and indiciesOfGearsTouchingCur:
                    for cords in indiciesOfGearsTouchingCur:
                        gearMap[cords].append(int(curNumStr))
                curNumStr = ""
                indiciesOfGearsTouchingCur =  set()
        if curNumStr and indiciesOfGearsTouchingCur:
            for cords in indiciesOfGearsTouchingCur:
                gearMap[cords].append(int(curNumStr))
    return gearMap

def isAdjacentToGear(input: List[List[str]], i, j, indxList):
    getGearCoords(input, i + 1, j, indxList)
    getGearCoords(input, i - 1, j, indxList)
    getGearCoords(input, i + 1, j + 1, indxList)
    getGearCoords(input, i - 1, j - 1, indxList) 
    getGearCoords(input, i, j + 1, indxList)
    getGearCoords(input, i, j - 1, indxList)
    getGearCoords(input, i + 1, j - 1, indxList)
    getGearCoords(input, i - 1, j + 1, indxList)             

def getGearCoords(input: list[list[str]], x, y, indxList):
    if x < 0 or x >= len(input) or y < 0 or y >= len(input[x]):
        return False

    char = input[x][y]
    if char == "*":
        indxList.add((x,y))
        

def sumofGearPower(gearMap):
    sum = 0

    for nums in gearMap.values():
        if len(nums) == 2:
            x, y = nums
            sum += x * y
    return sum

def solve():
    listInput = inputToList()
    gearMap = getGearMap(listInput)
    res = sumofGearPower(gearMap)
    print(res)

solve()
