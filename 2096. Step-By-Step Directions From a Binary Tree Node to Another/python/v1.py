from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:

        start_dirs = []
        dest_dirs = []
        found = False

        def recurse(node: Optional[TreeNode]):
            nonlocal startValue, destValue, start_dirs, dest_dirs, found
            if found or not node:
                return {}

            left = recurse(node.left)
            right = recurse(node.right)

            res = left | right
            if destValue in res:
                res[destValue].append("L" if destValue in left else "R")
            if startValue in res:
                res[startValue].append("U")

            if node.val == startValue and destValue in (left | right):
                found = True
                dest_dirs = left.get(destValue, []) + right.get(destValue, [])
                return {}
            if node.val == destValue and startValue in (left | right):
                found = True
                start_dirs = left.get(startValue, []) + right.get(startValue, [])
                return {}
            if startValue in (left | right) and destValue in (left | right):
                found = True
                start_dirs = left.get(startValue, []) + right.get(startValue, [])
                dest_dirs = left.get(destValue, []) + right.get(destValue, [])
                return {}

            if node.val == startValue:
                res[startValue] = []
            if node.val == destValue:
                res[destValue] = []

            return res

        recurse(root)

        return "".join(start_dirs + dest_dirs[::-1])
