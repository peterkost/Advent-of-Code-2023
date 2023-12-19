from utils.misc import Direction
from day10.Maze import Maze


UP, DOWN, LEFT, RIGHT = Direction


def makeMoveOn(maze: Maze) -> None:
    symbol, direction = maze.getCurrentSymbol(), maze.getCurrentDirection()

    if symbol in set(["|", "-"]):
        maze.move(direction)
    elif symbol == "L":
        maze.move(UP if direction == LEFT else RIGHT)
    elif symbol == "J":
        maze.move(UP if direction == RIGHT else LEFT)
    elif symbol =="7":
        maze.move(DOWN if direction == RIGHT else LEFT)
    elif symbol == "F":
        maze.move(DOWN if direction == LEFT else RIGHT)


def getLoopDistance(maze: Maze) -> int:
    makeMoveOn(maze)
    distance = 1

    while not maze.onStart():
        makeMoveOn(maze)
        distance += 1

    return distance


def solve():
    maze = Maze(False)
    distance = getLoopDistance(maze)
    print(distance // 2)

