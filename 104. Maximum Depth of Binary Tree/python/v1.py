from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node: Optional[TreeNode], current_level: int):
            if not node:
                return current_level - 1

            return max(
                max_depth(node.left, current_level + 1),
                max_depth(node.right, current_level + 1),
                current_level,
            )

        return max_depth(root, 1)
