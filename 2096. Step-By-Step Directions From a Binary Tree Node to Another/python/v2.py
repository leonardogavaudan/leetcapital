from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def dfs(node: TreeNode | None, target: int, path: List[str]) -> List[str]:
            if not node:
                return []

            if node.val == target:
                return path

            path.append("L")
            left_path = dfs(node.left, target, path)
            if left_path:
                return left_path
            path.pop()

            path.append("R")
            right_path = dfs(node.right, target, path)
            if right_path:
                return right_path
            path.pop()

            return []

        start_path = dfs(root, startValue, [])
        dest_path = dfs(root, destValue, [])

        i = 0
        while (
            i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]
        ):
            i += 1

        return "".join(["U"] * (len(start_path) - i) + dest_path[i:])
