from enum import Enum
from dataclasses import dataclass

class Part(Enum):
    ONE = 1
    TWO = 2

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


@dataclass
class Coords:
    x: int
    y: int

