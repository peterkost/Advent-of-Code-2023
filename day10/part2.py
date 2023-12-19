from typing import Set, Tuple
from day10.Maze import Maze
from day10.part1 import makeMoveOn


def getCoordsOfOurPipe(maze: Maze) -> Set[Tuple[int, int]]:
    coords = set()
    coords.add((maze.location.x, maze.location.y))
    makeMoveOn(maze)
    coords.add((maze.location.x, maze.location.y))
    while not maze.onStart():
        makeMoveOn(maze)
        coords.add((maze.location.x, maze.location.y))
    return coords


def countInternalPipes(maze: Maze, coords) -> int:
    map = maze.map
    total = 0
    for x in range(len(map)):
        betweenPipes = False
        curCount = 0
        openingBend = ""
        for y in range(len(map[0])):
            curSymbol = map[x][y]
            if (x, y) in coords:
                if curSymbol == "|":
                    total += curCount
                    curCount = 0
                    betweenPipes = not betweenPipes
                elif curSymbol in {"F", "L"}:
                    openingBend = curSymbol
                elif (curSymbol == "7" and openingBend == "L") or curSymbol == "J" and openingBend == "F":
                    betweenPipes = not betweenPipes
            elif betweenPipes:
                curCount += 1
        total += curCount
    return  total


def solve():
    maze = Maze(False)
    coords = getCoordsOfOurPipe(maze)
    internalPipes = countInternalPipes(maze, coords)
    print(internalPipes)

solve()
