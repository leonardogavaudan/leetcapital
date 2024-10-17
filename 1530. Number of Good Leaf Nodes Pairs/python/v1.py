from collections import defaultdict
from typing import DefaultDict, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0

        def recurse(node: Optional[TreeNode]) -> DefaultDict[int, int]:
            if not node:
                return defaultdict(int)

            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            nonlocal res
            left = recurse(node.left)
            right = recurse(node.right)

            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        res += left[d1] * right[d2]

            new_dist = defaultdict(int)

            for d in left:
                if d + 1 < distance:
                    new_dist[d + 1] += left[d]
            for d in right:
                if d + 1 < distance:
                    new_dist[d + 1] += right[d]

            return new_dist

        recurse(root)

        return res
