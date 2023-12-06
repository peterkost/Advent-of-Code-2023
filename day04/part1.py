import re
from typing import List, Set, Tuple
from collections import defaultdict
from utils.fileHelper import getLinesFor


def getWinningAndMyNumsFor(game: str) -> Tuple[Set[str], List[str]]:
    nums = re.sub(r'.*: ', '', game.strip())
    winningStr, myStr = nums.split(' | ')
    return (set(winningStr.split()), myStr.split())

def getNumWinnersIn(game: str) -> int:
    wins = 0
    winningNums, myNums = getWinningAndMyNumsFor(game)
    for num in myNums:
        if num in winningNums:
            wins += 1
    return wins

def getAndPrintAnswer():
    lines = getLinesFor(day="04", sample=False)

    instancesOf = defaultdict(int)
    gameNum = 1
    for game in lines:
        instancesOf[gameNum] += 1
        wins = getNumWinnersIn(game)
        for i in range(gameNum + 1, gameNum + wins + 1):
            instancesOf[i] += instancesOf[gameNum]
        gameNum += 1
    print(sum(instancesOf.values()))

if __name__ == "__main__":
   getAndPrintAnswer()
