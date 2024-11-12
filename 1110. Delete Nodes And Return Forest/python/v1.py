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

        res = [root]
        to_delete_set = set(to_delete)

        def recurse(node: TreeNode | None, to_delete_set: Set[int]):
            nonlocal res
            if not node:
                return None

            if node.val in to_delete_set:
                if node.left:
                    res.append(node.left)
                    recurse(node.left, to_delete_set)
                if node.right:
                    res.append(node.right)
                    recurse(node.right, to_delete_set)
                return None
            else:
                node.left = recurse(node.left, to_delete_set)
                node.right = recurse(node.right, to_delete_set)
                return node

        recurse(root, to_delete_set)
        res = [node for node in res if node.val not in to_delete_set]

        return res
