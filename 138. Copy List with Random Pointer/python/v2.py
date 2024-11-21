from typing import Optional


class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        new_head = None
        node = head
        prev_new_node = None
        new_node = None

        cache = {}

        while node:
            new_node = Node(node.val, None, node.random)
            if prev_new_node:
                prev_new_node.next = new_node
            if new_head is None:
                new_head = new_node

            cache[node] = new_node
            prev_new_node = new_node
            node = node.next

        node = new_head
        while node:
            if node.random:
                node.random = cache[node.random]

            node = node.next

        return new_head
