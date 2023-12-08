
class Node:
    def __init__(self, name, left = None, right = None):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Node: {self.name}, Left: {self.left.name if self.left else None}, Right: {self.right.name if self.right else None}"
