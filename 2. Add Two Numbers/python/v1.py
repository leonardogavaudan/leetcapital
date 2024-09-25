from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        prev: Optional[ListNode] = None
        res = ListNode()
        root = res

        while l1 is not None or l2 is not None:
            if l1 is not None:
                res.val += l1.val
                l1 = l1.next
            if l2 is not None:
                res.val += l2.val
                l2 = l2.next

            res.val += carry

            if res.val > 9:
                res.val = res.val % 10
                carry = 1
            else:
                carry = 0

            res.next = ListNode()
            prev = res
            res = res.next

        if carry == 1:
            res.val = 1
            return root

        if prev is None:
            raise ValueError()

        prev.next = None
        return root
