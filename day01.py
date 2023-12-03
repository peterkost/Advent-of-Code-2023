def getLines() -> list[str]:
    input = open("day01-input.txt", "r")
    return input.readlines()
    
def sumCalibrationValues(lines: list[str]) -> int:
    res = 0
    for line in lines:
        res += getValueOf(line)
    return res

def getValueOf(line: str) -> int:
    first, last = getDigit(line, True), getDigit(line, False)
    return int(first + last)

def getDigit(line: str, first: bool) -> str:
    rnge = range(len(line)) if first else range(len(line) - 1, -1, -1)
    for i in rnge:
        if line[i].isnumeric():
            return line[i]
    raise Exception(f"Couldn't find digit {'first' if first else 'last'} digit in {line}")


lines = getLines()
sum = sumCalibrationValues(lines)
print(sum)


