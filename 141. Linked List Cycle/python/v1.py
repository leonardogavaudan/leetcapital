from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        MARKED_VALUE = 10**6

        while head is not None:
            if head.val == MARKED_VALUE:
                return True

            head.val = MARKED_VALUE
            head = head.next

        return False
