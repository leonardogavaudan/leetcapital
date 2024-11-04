class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node):
        if not self.head.next:
            raise ValueError()
        self.head.next.prev, node.next = node, self.head.next
        self.head.next, node.prev = node, self.head

    def _remove(self, node: Node):
        if not node.prev or not node.next:
            raise ValueError()
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                if not lru:
                    raise IndexError()

                self._remove(lru)
                del self.cache[lru.key]
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)
