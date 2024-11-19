from typing import List, Optional


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
        targets = set(to_delete)
        res = [root]

        def recurse(node: TreeNode | None):
            if not node:
                return None

            if node.val in targets:
                if node.left:
                    res.append(node.left)
                    recurse(node.left)
                if node.right:
                    res.append(node.right)
                    recurse(node.right)
                return None
            else:
                node.left = recurse(node.left)
                node.right = recurse(node.right)
                return node

        recurse(root)
        res = [node for node in res if node.val not in targets]
        return res
