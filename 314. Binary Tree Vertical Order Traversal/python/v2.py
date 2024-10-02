from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        col_to_nodes = {}
        queue = deque([(0, root)])
        min_col, max_col = float("inf"), float("-inf")

        while queue:
            col, node = queue.popleft()

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if col not in col_to_nodes:
                col_to_nodes[col] = []

            col_to_nodes[col].append(node.val)

            if node.left:
                queue.append((col - 1, node.left))

            if node.right:
                queue.append((col + 1, node.right))

        for i in range(int(min_col), int(max_col + 1)):
            res.append(col_to_nodes[i])

        return res
