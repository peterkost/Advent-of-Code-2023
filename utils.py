from enum import Enum

class Part(Enum):
    ONE = 1
    TWO = 2

def getLinesFor(day: str, sample: bool = False) -> list[str]:
    input = open(f"day{day}-input{'-sample' if sample else ''}.txt", "r")
    return input.readlines()
