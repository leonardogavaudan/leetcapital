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
            return

        new_head = None
        prev = None
        old_to_new = {}

        while head:
            new_node = Node(head.val, None, head.random)
            if prev:
                prev.next = new_node

            if not new_head:
                new_head = new_node

            old_to_new[head] = new_node
            prev = new_node
            head = head.next

        node = new_head
        while node:
            if node.random:
                node.random = old_to_new[node.random]
            node = node.next

        return new_head
