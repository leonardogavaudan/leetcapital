from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Optional[Node], q: Optional[Node]) -> Node:
        seen_p = set()
        seen_q = set()

        while p or q:
            if p:
                if p.val in seen_q:
                    return p

                seen_p.add(p.val)
                p = p.parent

            if q:
                if q.val in seen_p:
                    return q

                seen_q.add(q.val)
                q = q.parent

        raise ValueError("not found")
