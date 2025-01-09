import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        counter = len(lists)
        heapq.heapify(heap)

        head = ListNode(0)
        current = head

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = node

            node = node.next
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        return head.next
