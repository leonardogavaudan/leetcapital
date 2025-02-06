from itertools import islice
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        COLS = len(matrix[0])
        prev_row = list(map(lambda x: int(x), matrix[0]))
        max_square_length = max(prev_row)

        for row in islice(matrix, 1, None):
            curr_row = [
                prev_row[i] + int(row[i]) if row[i] != "0" else 0 for i in range(COLS)
            ]

            for length in range(max_square_length + 1, COLS + 1):
                count = 0
                for i in range(COLS):
                    if curr_row[i] >= length:
                        count += 1
                        if count == length:
                            max_square_length = length
                    else:
                        count = 0
            prev_row = curr_row

        return max_square_length**2
