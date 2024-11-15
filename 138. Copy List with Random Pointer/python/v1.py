class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        if not head:
            return None

        node = head
        old_to_new = {}
        prev: Node | None = None
        new_head: Node | None = None
        while node:
            new_node = Node(node.val, None, node.random)
            if prev:
                prev.next = new_node
            if not new_head:
                new_head = new_node

            old_to_new[node] = new_node
            prev = new_node
            node = node.next

        node = new_head
        while node:
            if node.random:
                node.random = old_to_new[node.random]
            node = node.next

        return new_head
