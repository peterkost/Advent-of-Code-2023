from utils import Part, getLinesFor


class MAX:
    RED = 12
    GREEN = 13
    BLUE = 14

class Game:
    def __init__(self, rawLine: str):
        self._parseLine(rawLine)

    def _parseLine(self, input: str):
        idPortion, roundsPortion = input.split(": ")

        self.id = Game._parseId(idPortion)
        self.maxRed, self.maxGreen, self.maxBlue = Game._parseRounds(roundsPortion) 

    def __str__(self) -> str:
        return  f"ID: {self.id}, red: {self.maxRed}, green: {self.maxGreen}, blue: {self.maxBlue}"


    @staticmethod
    def _parseId(rawId: str) -> int:
        strId = rawId.replace("Game ", "")
        return int(strId)

    @staticmethod
    def _parseRounds(rawRounds: str) -> tuple[int, int, int]:
        red = green = blue = -1

        splitRounds = rawRounds.split("; ")
        for round in splitRounds:
            roundParts = round.split(", ")
            for roundPart in roundParts:
                countStr, colorStr = roundPart.split(" ")
                count = int(countStr)
                match colorStr:
                    case"red":
                        red = max(red, count)
                    case "green":
                        green = max(green, count)
                    case "blue":
                        blue = max(blue, count)
                    case _:
                        raise Exception("Unable to parse color")
        return (red, green, blue)


def inputToGame(sample: bool = False) -> list[Game]:
    res = []
    lines = getLinesFor(day="02", sample=sample)
    for line in lines:
        res.append(Game(line.strip()))
    return res

def sumOfValidGameIds(games: list[Game]) -> int:
    sum = 0
    for game in games:
        if game.maxRed <= MAX.RED and game.maxGreen <= MAX.GREEN and game.maxBlue <= MAX.BLUE:
            sum += game.id
    return sum

def sumOfPowerSets(games: list[Game]) -> int:
    sum = 0
    for game in games:
        sum += game.maxBlue * game.maxGreen * game.maxRed
    return sum

def solve(part: Part):
    games = inputToGame()
    sum = sumOfValidGameIds(games) if part == Part.ONE else sumOfPowerSets(games)
    print(sum)

solve(Part.TWO)
