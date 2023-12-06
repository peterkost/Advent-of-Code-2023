import re
from utils.fileHelper import getLinesFor


def getAndPrintAnswer():
    lines = getLinesFor(day="04", sample=False)

    sum = 0
    for game in lines:
        nums = re.sub(r'.*: ', '', game.strip())
        winningStr, myStr = nums.split(' | ')
        winningNums, myNums = winningStr.split(), myStr.split()
        
        gameTotal = 0
        for num in myNums:
            if num in winningNums:
                if not gameTotal:
                    gameTotal = 1
                else:
                    gameTotal *= 2
        sum += gameTotal

    print(sum)


if __name__ == "__main__":
   getAndPrintAnswer()

