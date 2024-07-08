from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        queue = deque([root])
        res = 0

        while queue:
            current_node = queue.popleft()
            if current_node is None:
                continue
            if low <= current_node.val <= high:
                res += current_node.val
                queue.append(current_node.left)
                queue.append(current_node.right)
            if current_node.val < low:
                queue.append(current_node.right)
            if current_node.val > high:
                queue.append(current_node.left)

        return res
