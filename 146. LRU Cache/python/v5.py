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
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node: Node) -> None:
        if not self.head.next:
            raise IndexError()
        temp = self.head.next
        self.head.next.prev = self.head.next = node
        node.prev, node.next = self.head, temp

    def _remove(self, node: Node) -> None:
        if not node.prev or not node.next:
            raise IndexError()
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
            self._remove(node)
            self._add(node)
            node.value = value
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                if not lru:
                    raise IndexError()
                del self.cache[lru.key]
                self._remove(lru)

            node = Node(key, value)
            self.cache[key] = node
            self._add(node)
