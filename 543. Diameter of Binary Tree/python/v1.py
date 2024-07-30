from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left_subtree_height = dfs(node.left)
            right_subtree_height = dfs(node.right)

            self.diameter = max(
                self.diameter, left_subtree_height + right_subtree_height
            )

            return max(left_subtree_height, right_subtree_height) + 1

        dfs(root)

        return self.diameter
