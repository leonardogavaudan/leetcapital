from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]

        def is_critical(prev: ListNode, curr: ListNode):
            return curr.next and (
                prev.val < curr.val > curr.next.val
                or prev.val > curr.val < curr.next.val
            )

        min_dist, max_dist = float("inf"), float("-inf")
        prev, curr = head, head.next
        while curr and not is_critical(prev, curr):
            prev = curr
            curr = curr.next

        if not curr:
            return [-1, -1]

        prev = curr
        curr = curr.next
        dist_from_initial = 1
        dist_from_prev = 1

        while curr:
            if is_critical(prev, curr):
                min_dist = min(min_dist, dist_from_prev)
                max_dist = dist_from_initial
                dist_from_prev = 0

            prev = curr
            curr = curr.next
            dist_from_initial += 1
            dist_from_prev += 1

        return [int(min_dist), int(max_dist)] if isinstance(min_dist, int) else [-1, -1]
