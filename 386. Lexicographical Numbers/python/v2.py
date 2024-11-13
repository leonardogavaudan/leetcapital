from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(number: int, n: int, res: List[int]):
            if number > n:
                return
            res.append(number)

            for i in range(10):
                new_number = number * 10 + i
                dfs(new_number, n, res)

        for i in range(1, 10):
            dfs(i, n, res)

        return res
