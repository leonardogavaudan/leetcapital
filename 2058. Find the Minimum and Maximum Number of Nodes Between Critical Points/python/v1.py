from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]

        def is_critical(prev, current, next):
            return (prev.val < current.val > next.val) or (
                prev.val > current.val < next.val
            )

        prev = head
        current = head.next
        next = current.next
        if not next:
            return [-1, -1]

        while next and not is_critical(prev, current, next):
            prev = current
            current = next
            next = next.next

        if not next:
            return [-1, -1]

        position = 1
        prev_crit_pos = 0
        min_dist, max_dist = float("inf"), 0

        prev = current
        current = next
        next = next.next

        while next:
            if is_critical(prev, current, next):
                min_dist = min(min_dist, position - prev_crit_pos)
                max_dist = position
                prev_crit_pos = position

            prev = current
            current = next
            next = next.next
            position += 1

        return [int(min_dist), max_dist] if max_dist != 0 else [-1, -1]
