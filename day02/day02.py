from utils.misc import Part
from utils.fileHelper import getLinesFor
from day02.game import Game

class MAX:
    RED = 12
    GREEN = 13
    BLUE = 14

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
