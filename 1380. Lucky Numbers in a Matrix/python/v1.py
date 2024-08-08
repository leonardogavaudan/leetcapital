from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []

        row_min_i_to_col_i = [-1] * len(matrix)
        col_max_i_to_row_i = [-1] * len(matrix[0])

        col_i_to_max_value = [0] * len(matrix[0])

        for row in range(len(matrix)):
            min_row_value = float("inf")

            for col in range(len(matrix[0])):
                if min_row_value > matrix[row][col]:
                    min_row_value = matrix[row][col]
                    row_min_i_to_col_i[row] = col

                if col_i_to_max_value[col] < matrix[row][col]:
                    col_i_to_max_value[col] = matrix[row][col]
                    col_max_i_to_row_i[col] = row

        for row_i, col_i in enumerate(row_min_i_to_col_i):
            if col_max_i_to_row_i[col_i] == row_i:
                res.append(matrix[row_i][col_i])

        return res
