from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROW, COL = len(rowSum), len(colSum)
        res = [[0] * COL for _ in range(ROW)]

        for row_i in range(ROW):
            res[row_i][0] = rowSum[row_i]

        for col_i in range(COL):
            current_col_total = 0
            for i in range(ROW):
                current_col_total += res[i][col_i]

            row_i = 0
            while current_col_total > colSum[col_i]:
                diff = current_col_total - colSum[col_i]
                shift = min(diff, res[row_i][col_i])
                current_col_total -= shift
                res[row_i][col_i] -= shift
                res[row_i][col_i + 1] += shift
                row_i += 1

        return res
