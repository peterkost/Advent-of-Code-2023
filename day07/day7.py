from typing import List, Tuple
from day07.Hand import Hand
from utils.fileHelper import getLinesFor

def sumHands(hands: List[Hand]) -> int:
    res = 0
    for i in range(len(hands)):
        res += hands[i].bet * (i + 1)
    return res

def solve():
    lines = getLinesFor("07", sample=True)
    hands = [Hand(line) for line in lines]
    hands.sort(reverse=True)
    [print(card) for card in hands]
    print(sumHands(hands))

