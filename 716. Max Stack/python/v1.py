import heapq


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None
        self.is_valid = True


class MaxStack:
    def __init__(self):
        self.heap = []
        self.tail = Node(0)
        self.head = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.counter = 0

    def _add_node(self, node: Node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def _remove_node(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev

    def push(self, x: int) -> None:
        node = Node(x)
        self._add_node(node)
        heapq.heappush(self.heap, (-x, -self.counter, node))
        self.counter += 1

    def pop(self) -> int:
        node = self.tail.prev
        node.is_valid = False
        self._remove_node(node)
        return node.value

    def top(self) -> int:
        return self.tail.prev.value

    def peekMax(self) -> int:
        while self.heap and not self.heap[0][2].is_valid:
            heapq.heappop(self.heap)
        return self.heap[0][2].value

    def popMax(self) -> int:
        while self.heap and not self.heap[0][2].is_valid:
            heapq.heappop(self.heap)
        val, _, node = heapq.heappop(self.heap)
        self._remove_node(node)
        node.is_valid = False
        return -val
