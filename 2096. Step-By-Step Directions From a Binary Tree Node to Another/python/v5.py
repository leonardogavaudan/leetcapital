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
        if not root:
            return ""

        def recurse(node: TreeNode | None, target: int, path: List[str]):
            if not node:
                return []

            if node.val == target:
                return path

            path.append("L")
            leftPath = recurse(node.left, target, path)
            if leftPath:
                return leftPath
            path.pop()

            path.append("R")
            rightPath = recurse(node.right, target, path)
            if rightPath:
                return rightPath
            path.pop()

            return []

        startPath = recurse(root, startValue, [])
        destPath = recurse(root, destValue, [])

        i = 0
        while i < min(len(startPath), len(destPath)):
            if startPath[i] != destPath[i]:
                break
            i += 1

        return "".join(["U"] * (len(startPath) - i) + destPath[i:])
