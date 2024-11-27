from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        prev_row = [0] * len(points[0])
        current_row = []
        i = 0
        while i < len(points):
            current_row = points[i]
            left = [
                (
                    prev_row[j]
                    if j == 0 or prev_row[j - 1] - 1 < prev_row[j]
                    else prev_row[j - 1] - 1
                )
                for j in range(len(prev_row))
            ]
            right = [
                (
                    prev_row[j]
                    if (j == (len(prev_row) - 1)) or prev_row[j + 1] - 1 < prev_row[j]
                    else prev_row[j + 1] - 1
                )
                for j in range(len(prev_row) - 1, -1, -1)
            ][::-1]

            for j in range(len(current_row)):
                current_row[j] = current_row[j] + max(left[j], right[j])

            i += 1
            prev_row = current_row

        return max(current_row)
