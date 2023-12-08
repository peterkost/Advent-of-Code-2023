from typing import List
from utils.fileHelper import getLinesFor
from day08.Node import Node
import re

def buildNodesFrom(lines: List[str]) -> Node:
    nodeMap = {}
    for line in lines:
        name = line.split()[0]
        nodeMap[name] = Node(name)

    r = re.compile("[A-Z]{3}")
    for line in lines:
        nodeName, left, right = r.findall(line)
        node = nodeMap[nodeName]
        node.left, node.right = nodeMap[left], nodeMap[right]
    return nodeMap["AAA"]

def countSteps(start: Node, moves):
    steps, cur, i = 0, start, 0
    n = len(moves)
    while cur.name != "ZZZ":
        move = moves[i % n]
        cur = cur.left if move == "L" else cur.right
        i += 1
        steps += 1



    return steps

def solve():
    lines = getLinesFor(day="08")
    start = buildNodesFrom(lines[2:])
    steps = countSteps(start, lines[0])
    print(steps)


solve()
