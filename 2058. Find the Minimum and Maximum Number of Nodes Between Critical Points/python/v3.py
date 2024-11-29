from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or head.next:
            return [-1, -1]

        def is_crit(head: ListNode, prev: ListNode | None):
            if not prev or not head.next:
                return False

            return (prev.val < head.val < head.next.val) or (
                prev.val > head.val < head.next.val
            )

        prev, head = head, head.next
        while head and not is_crit(head, prev):
            prev = head
            head = head.next
        if not head:
            return [-1, -1]

        max_dist = float("-inf")
        min_dist = float("inf")
        dist_from_prev = 0
        dist_from_initial = 0

        prev = head
        head = head.next
        while head:
            dist_from_prev += 1
            dist_from_initial += 1

            if is_crit(head, prev):
                max_dist = dist_from_initial
                min_dist = min(min_dist, dist_from_prev)
                dist_from_prev = 0

            prev = head
            head = head.next

        return [int(min_dist), int(max_dist)] if isinstance(min_dist, int) else [-1, -1]
