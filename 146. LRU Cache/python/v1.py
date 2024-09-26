from typing import Dict, Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node) -> None:
        if self.right.prev is None:
            raise IndexError

        prev, next = self.right.prev, self.right

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def delete(self, node: Node) -> None:
        prev, next = node.prev, node.next
        if prev is None or next is None:
            raise IndexError

        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_recent = self.left.next
            if least_recent is None:
                raise IndexError()
            self.delete(least_recent)
            del self.cache[least_recent.key]
