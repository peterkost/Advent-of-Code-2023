from typing import List
from utils.fileHelper import getLinesFor
from dataclasses import dataclass
from utils.misc import Part
from day12.classes import *


WORKING, BROKEN, ANY = ".", "#", "?"

def parse(part: Part) -> List[Line]:
    lines = getLinesFor(day="12", sample=True)
    records = []

    for line in lines:
        a, b = line.split()
        a, b = list(a), [int(n) for n in b.split(",")]
        if part == Part.TWO:
            a.append(ANY)
            a = a * 5
            b = b * 5
        records.append(Line(a, b))

    return records

def arrangements(line: Line, state: State, memo = {}):
    if state in memo:
        return memo[state]

    if state.springI == len(line.springs):
        # TODO - why satte.dmgLen != 0
        if state.dmgLen and state.dmgLen != line.checksum[state.csI]:
            return 0
        else:
            return 


def solve():
    records = parse(Part.ONE)
    [print(r) for r in records]

solve()
