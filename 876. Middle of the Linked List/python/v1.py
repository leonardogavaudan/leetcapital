from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        linked_list_length = 0
        temp = head
        while temp:
            temp = temp.next
            linked_list_length += 1

        for _ in range(linked_list_length // 2):
            head = head.next

        return head
