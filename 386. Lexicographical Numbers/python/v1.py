from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(current: int):
            nonlocal n, res
            if current > n:
                return

            res.append(current)

            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            if i > n:
                break
            dfs(i)

        return res
