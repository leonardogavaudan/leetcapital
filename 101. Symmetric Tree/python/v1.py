from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recurse(node1, node2):
            if not node1 and not node2:
                return True

            return (
                getattr(node1, "val", None) == getattr(node2, "val", None)
                and recurse(node1.left, node2.right)
                and recurse(node1.right, node2.left)
            )

        return recurse(root, root)
