from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def bfs(path: List[TreeNode], node: TreeNode | None, target: int):
            if not node:
                return []
            path.append(node)
            if node.val == target:
                return path

            left_path = bfs(path, node.left, target)
            if left_path:
                return left_path
            right_path = bfs(path, node.right, target)
            if right_path:
                return right_path

            path.pop()
            return []

        p_path = bfs([], root, p.val)
        q_path = bfs([], root, q.val)

        i = min(len(p_path), len(q_path)) - 1
        while i >= 0:
            if p_path[i].val == q_path[i].val:
                return p_path[i]
            i -= 1

        raise ValueError("No solution")
