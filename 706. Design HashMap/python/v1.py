from typing import List, Optional


class Node:
    def __init__(self, key, value) -> None:
        self.next = None
        self.key = key
        self.value = value


class MyHashMap:

    def __init__(self):
        self.arr: List[Optional[int]] = [None] * 1000

    def get_hash(self, key: int) -> int:
        return key % 1000

    def put(self, key: int, value: int) -> None:
        hash_ = self.get_hash(key)
        current_node = self.arr[hash_]
        prev = None
        while current_node is not None and current_node.key != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            new_node = Node(key, value)
            if prev is None:
                self.arr[hash_] = new_node
            else:
                prev.next = new_node
        else:
            current_node.value = value

    def get(self, key: int) -> int:
        hash_ = self.get_hash(key)
        current_node = self.arr[hash_]
        while current_node is not None and current_node.key != key:
            current_node = current_node.next

        if current_node is None:
            return -1

        return current_node.value

    def remove(self, key: int) -> None:
        hash_ = self.get_hash(key)
        current_node = self.arr[hash_]
        if current_node is None:
            return

        prev = None
        while current_node is not None and current_node.key != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        if prev is None:
            self.arr[hash_] = current_node.next
        else:
            prev.next = current_node.next
