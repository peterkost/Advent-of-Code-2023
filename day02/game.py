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
