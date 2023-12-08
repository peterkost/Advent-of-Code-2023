from collections import Counter, defaultdict
from enum import Enum
from typing import List

PART = 2

class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    def __init__(self, input: str):
        cards, bet = input.split()
        self.cards, self.bet = cards, int(bet)
        self.type = self._getType(cards)

    def __lt__(self, other):
        if self.type.value != other.type.value:
            return self.type.value > other.type.value
        else:
            return self._cardsToTieBreakerString(self.cards) > self._cardsToTieBreakerString(other.cards)

    @staticmethod
    def _cardsToTieBreakerString(cards: str) -> str:
        res = ""
        for card in cards:
            match card:
                case "A":
                    res += "Z"
                case "K":
                    res += "Y"
                case "Q":
                    res += "X"
                case "J":
                    res += "W" if PART == 1 else "M"
                case "T":
                    res += "V"
                case "9":
                    res += "U"
                case "8":
                    res += "T"
                case "7":
                    res += "S"
                case "6":
                    res += "R"
                case "5":
                    res += "Q"
                case "4":
                    res += "P"
                case "3":
                    res += "O"
                case "2":
                    res += "N"
        return res


    def __str__(self):
        return f"Cards: {self.cards} - Type: {self.type} - Bet: {self.bet}"

    @staticmethod
    def _getType(cards: str) -> Type:
        cardCount = Hand._getCardCount(cards)
        if 5 in cardCount:
            return Type.FIVE_OF_A_KIND
        elif 4 in cardCount:
            return Type.FOUR_OF_A_KIND
        elif len(cardCount) == 2:
            return Type.FULL_HOUSE
        elif 3 in cardCount:
            return Type.THREE_OF_A_KIND
        elif cardCount.count(2) == 2:
            return Type.TWO_PAIR
        elif 2 in cardCount:
            return Type.ONE_PAIR
        else:
            return Type.HIGH_CARD

    @staticmethod
    def _getCardCount(cards: str) -> List[int]:
        if PART == 1:
            return list(Counter(cards).values())
        else:
            print(cards)
            count = defaultdict(int)
            jCount = 0
            for card in cards:
                if card == "J":
                    jCount += 1
                else:
                    count[card] += 1
            res = list(count.values())
            res.sort(reverse=True)
            if res:
                res[0] += jCount
            else: 
                res = [jCount]
            return  res


