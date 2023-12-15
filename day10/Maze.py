from typing import List
from dataclasses import dataclass
from utils.fileHelper import getLinesFor
from utils.misc import Direction

UP, DOWN, LEFT, RIGHT = Direction

class Maze:
    @dataclass
    class Location:
        x: int
        y: int
        direction: Direction


    def __init__(self, useSampleInput: bool = True):
        self.map = Maze._drawMap(useSampleInput)
        self.location = self._getStartLocation()
        self._getOffStart()
    

    @staticmethod
    def _drawMap(useSampleInput: bool) -> List[List[str]]:
        lines = getLinesFor(day="10", sample=useSampleInput)
        return [list(line) for line in lines]


    def _getStartLocation(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                if self.map[x][y] == "S":
                    return self.Location(x, y, DOWN)
        raise Exception("Can't even find the start of this thing!")


    def _getOffStart(self):
        x, y, m = self.location.x, self.location.y, self.map

        above = m[x - 1][y] if x > 0 else "."
        bellow = m[x + 1][y] if x < len(m) - 1 else "."
        left = m[x][y - 1] if y > 0 else "."
        right = m[x][y + 1] if y < len(m[0]) - 1 else "."
    
        if above in set(["|", "7", "F"]):
            self.move(UP)
            self.changeDirection(to=UP)
        elif bellow in set(["|", "L", "J"]):
            self.move(DOWN)
            self.changeDirection(to=DOWN)
        elif left in set(["-", "L", "F"]):
            self.move(LEFT)
            self.changeDirection(to=LEFT)
        elif right in set(["-", "J", "7"]):
            self.move(RIGHT)
            self.changeDirection(to=RIGHT)
    
        if self.getCurrentSymbol() in set(["S", "."]):
            raise Exception("First move and we already messed up!")


    def getCurrentSymbol(self) -> str:
        return self.map[self.location.x][self.location.y]


    def getCurrentDirection(self) -> Direction:
        return self.location.direction


    def move(self, direction: Direction) -> None:
        match direction:
            case Direction.UP:
                self.location.x -= 1
            case Direction.DOWN:
                self.location.x += 1
            case Direction.LEFT:
                self.location.y -= 1
            case Direction.RIGHT:
                self.location.y += 1

        self.changeDirection(direction) 

        if self.getCurrentSymbol() == ".":
            raise Exception("You must have taken a wrong turn, you are off the map!")


    def changeDirection(self, to: Direction) -> None:
        self.location.direction = to
