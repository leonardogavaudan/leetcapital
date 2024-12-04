from typing import Dict, List, Set


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.parents: Set[Node] = set()
        self.children: Dict[Node, int] = {}

    def update_val(self, diff: int):
        self.value += diff
        for parent in self.parents:
            multiplier = parent.children.get(self, 1)
            parent.update_val(diff * multiplier)

    def release_children(self):
        for child in self.children:
            child.parents.remove(self)
        self.children.clear()


class Excel:
    def __init__(self, height: int, width: str):
        self.nodes = {}

    def set(self, row: int, column: str, val: int) -> None:
        if (row, column) not in self.nodes:
            self.nodes[(row, column)] = Node(val)
        else:
            node = self.nodes[(row, column)]
            node.update_val(val - node.value)
            node.release_children()
            node.children = {}

    def get(self, row: int, column: str) -> int:
        return self.nodes[(row, column)].value if (row, column) in self.nodes else 0

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        total = 0
        parent = self.nodes.get((row, column), Node(0))
        parent.release_children()

        children = []
        for number in numbers:
            if len(number) == 2:
                r, c = (int(number[1:]), number[0])
                if (r, c) not in self.nodes:
                    self.nodes[(r, c)] = Node(0)
                children.append(self.nodes[(r, c)])
            else:
                r1, r2 = int(number.split(":")[0][1:]), int(number.split(":")[1][1:])
                c1, c2 = number[0], number.split(":")[1][0]
                for r in range(r1, r2 + 1):
                    for c in range(ord(c1), ord(c2) + 1):
                        c = chr(c)
                        if (r, c) not in self.nodes:
                            self.nodes[(r, c)] = Node(0)
                        children.append(self.nodes[(r, c)])
        for node in children:
            total += node.value
            if node not in parent.children:
                parent.children[node] = 0
            parent.children[node] += 1
            node.parents.add(parent)
        parent.update_val(total - parent.value)
        self.nodes[(row, column)] = parent
        return total
