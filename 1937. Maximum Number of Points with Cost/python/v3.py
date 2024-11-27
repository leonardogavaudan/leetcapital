from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        prev_row = [0] * len(points[0])
        current_row = []
        i = 0
        while i < len(points):
            current_row = points[i].copy()
            left = [prev_row[0]]
            for j in range(1, len(prev_row)):
                left.append(max(left[-1] - 1, prev_row[j]))

            right = [prev_row[-1]]
            for j in range(len(prev_row) - 2, -1, -1):
                right.append(max(right[-1] - 1, prev_row[j]))
            right = right[::-1]

            for j in range(len(current_row)):
                current_row[j] = current_row[j] + max(left[j], right[j])

            i += 1
            prev_row = current_row

        return max(current_row)
