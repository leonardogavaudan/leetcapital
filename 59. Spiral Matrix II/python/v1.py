from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        c = 1
        for iteration in range((n + 1) // 2):
            start = iteration
            end = n - iteration - 1

            # top
            for i in range(start, end + 1):
                res[start][i] = c
                c += 1
            if start == end:
                break

            # right
            for i in range(start + 1, end):
                res[i][end] = c
                c += 1

            # bottom
            for i in range(end, start - 1, -1):
                res[end][i] = c
                c += 1

            # left
            for i in range(end - 1, start, -1):
                res[i][start] = c
                c += 1

        return res
