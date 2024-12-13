from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def find_path(
            node: TreeNode | None, path: List[TreeNode], target: int
        ) -> List[TreeNode]:
            if not node:
                return []

            path.append(node)

            if node.val == target:
                return path

            left_path = find_path(node.left, path, target)
            if left_path:
                return left_path

            right_path = find_path(node.right, path, target)
            if right_path:
                return right_path

            path.pop()

            return []

        p_path = find_path(root, [], p.val)
        q_path = find_path(root, [], q.val)

        i = 0
        while i < min(len(p_path), len(q_path)) and p_path[i].val == q_path[i].val:
            i += 1

        return p_path[i - 1]
