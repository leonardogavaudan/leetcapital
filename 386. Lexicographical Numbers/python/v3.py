from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def recurse(num: int, n: int):
            if num > n:
                return
            nonlocal res
            res.append(num)
            for d in range(10):
                recurse(num * 10 + d, n)

        for i in range(1, 10):
            recurse(i, n)

        return res
