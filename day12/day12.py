from typing import List
from utils.fileHelper import getLinesFor
from dataclasses import dataclass


# I would like acknowledge this code is ugo


OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


@dataclass
class Record:
    conditionRecord: List[str]
    damagedSpringSizes: List[int]

    def __str__(self) -> str:
        return f"{self.conditionRecord} {','.join(map(str, self.damagedSpringSizes))}"


def getRecords() -> List[Record]:
    lines = getLinesFor(day="12", sample=False)
    records = []

    for line in lines:
        a, b = line.split()
        records.append(Record(list(a), [int(n) for n in b.split(",")]))

    return records


def getArrangementSum(records: List[Record]) -> int:
    count = 0
    for record in records:
        thisOne = 0
        possibilities = []
        generatePossibilities(record.conditionRecord, 0, possibilities)
        for pos in possibilities:
            p = list(filter(None, "".join(pos).split(".")))
            if len(p) == len(record.damagedSpringSizes):
                if all([len(a) == b for a, b in zip(p, record.damagedSpringSizes)]): 
                    thisOne += 1
        count += thisOne
    return count


def generatePossibilities(condition: List[str], i: int, res: List[List[str]]):
    if i == len(condition):
        res.append(condition)
        return
    if condition[i] == UNKNOWN:
        placeSpace = condition[:]
        placeSpace[i] = OPERATIONAL
        generatePossibilities(placeSpace, i + 1, res)

        placeBroken = condition[:]
        placeBroken[i] = DAMAGED
        generatePossibilities(placeBroken, i + 1, res)
    else:
        generatePossibilities(condition[:], i + 1, res)


def solve():
    records = getRecords()
    sum = getArrangementSum(records)
    print(sum)


solve()
