from utils import getLinesFor


PART1 = False


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
        cur = digit(line, i)
        if cur[0]:
            return cur[1]
    raise Exception(f"Couldn't find digit {'first' if first else 'last'} digit in {line}")

# returns [isDigit, digitAsNumeralString]
def digit(line: str, i) -> tuple[bool, str]:
    if PART1 or line[i].isnumeric():
        return (line[i].isnumeric(), line[i])
    else:
        return isWordADigit(line, i) 

# PART 2
FIRST_LETTERS = set(["o", "t", "f", "s", "e", "n"])
POSSIBLE_NUMS = {"o":["one"], "t":["two", "three"], "f":["four", "five"], "s":["six", "seven"], "e":["eight"], "n":["nine"]}
WORD_TO_NUM = {"one": "1", "two": "2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def isWordADigit(line: str, i) -> tuple[bool, str]:
    if line[i] in FIRST_LETTERS:
        for number in POSSIBLE_NUMS[line[i]]:
            end = i + len(number)
            if i + len(number) <= len(line) and line[i:end] == number:
                return (True, WORD_TO_NUM[number])
    return (False, "")

lines = getLinesFor(day="01")
sum = sumCalibrationValues(lines)
print(sum)


