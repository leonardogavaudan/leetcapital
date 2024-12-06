class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev: Node | None = None
        self.next: Node | None = None


class AllOne:
    def __init__(self):
        self.head = Node(float("-inf"))
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_map = {}

    def _add_node_after(self, node, count):
        new_node = Node(count)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        return new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_map:
            node = self.head.next
            if not node:
                raise IndexError()

            if node == self.tail or node.count > 1:
                node = self._add_node_after(self.head, 1)
            node.keys.add(key)
            self.key_map[key] = (1, node)
        else:
            count, node = self.key_map[key]
            new_count = count + 1
            node.keys.remove(key)
            if node.next == self.tail or node.next.count > new_count:
                node_next = self._add_node_after(node, new_count)
            else:
                node_next = node.next
            node_next.keys.add(key)
            self.key_map[key] = (new_count, node_next)
            if len(node.keys) == 0:
                self._remove_node(node)

    def dec(self, key: str) -> None:
        count, node = self.key_map[key]
        new_count = count - 1
        node.keys.remove(key)
        if new_count == 0:
            del self.key_map[key]
        else:
            if node.prev == self.head or node.prev.count < new_count:
                node_prev = self._add_node_after(node.prev, new_count)
            else:
                node_prev = node.prev
            node_prev.keys.add(key)
            self.key_map[key] = (new_count, node_prev)
        if len(node.keys) == 0:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        if not self.tail.prev:
            raise IndexError()
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        if not self.head.next:
            raise IndexError()
        return next(iter(self.head.next.keys))
