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
        def dfs(node: TreeNode | None, path: List[str], target: int):
            if not node:
                return []
            if node.val == target:
                return path

            path.append("L")
            left_path = dfs(node.left, path, target)
            if left_path:
                return left_path
            path.pop()

            path.append("R")
            right_path = dfs(node.right, path, target)
            if right_path:
                return right_path
            path.pop()

            return []

        start_path = dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)

        i = 0
        while (
            i < min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]
        ):
            i += 1

        return "".join(len(start_path[i:]) * ["U"] + dest_path[i:])
