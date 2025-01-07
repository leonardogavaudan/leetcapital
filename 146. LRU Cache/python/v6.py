class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: Node):
        assert node.prev and node.next
        node.prev.next, node.next.prev = node.next, node.prev

    def _add(self, node: Node):
        assert self.head.next
        node.next, self.head.next.prev = self.head.next, node
        self.head.next, node.prev = node, self.head

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.table) == self.capacity:
                lru = self.tail.prev
                assert lru
                self._remove(lru)
                del self.table[lru.key]

            node = Node(key, value)
            self._add(node)
            self.table[key] = node
