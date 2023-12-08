from typing import List
from utils.fileHelper import getLinesFor
from day08.Node import Node
import re
from math import lcm

PART = 2

def buildNodesFrom(lines: List[str]) -> List[Node]:
    nodeMap = {}
    for line in lines:
        name = line.split()[0]
        nodeMap[name] = Node(name)

    r = re.compile("[A-Z0-9]{3}")
    starts = []
    for line in lines:
        nodeName, left, right = r.findall(line)
        node = nodeMap[nodeName]
        node.left, node.right = nodeMap[left], nodeMap[right]
        if (PART == 1 and nodeName == "AAA") or (PART == 2 and nodeName[-1] == "A"):
            starts.append(node)
    return starts

def countSteps(start: Node, moves):
    steps, cur, i = 0, start, 0
    n = len(moves)
    while not isEnd(cur):
        move = moves[i % n]
        cur = cur.left if move == "L" else cur.right
        i += 1
        steps += 1
    return steps

def isEnd(node: Node) -> bool:
    return node.name == "ZZZ" if PART == 1 else node.name[-1] == "Z"

def solve():
    lines = getLinesFor(day="08")
    starts = buildNodesFrom(lines[2:])
    steps = []
    for start in starts:
        steps.append(countSteps(start, lines[0]))
    print(lcm(*steps))


solve()
