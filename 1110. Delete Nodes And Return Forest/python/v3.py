from typing import List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if not root:
            return []

        def recurse(node: Optional[TreeNode], to_delete: Set[int], res: List[TreeNode]):
            if not node:
                return None

            node.left = recurse(node.left, to_delete, res)
            node.right = recurse(node.right, to_delete, res)

            if node.val in to_delete:
                if node.right:
                    res.append(node.right)
                if node.left:
                    res.append(node.left)
                return None
            else:
                return node

        to_delete_set = set(to_delete)
        res = [root]
        recurse(root, to_delete_set, res)
        return [node for node in res if node.val not in to_delete_set]
