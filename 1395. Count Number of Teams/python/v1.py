from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for j in range(1, len(rating) - 1):
            left_smaller, left_bigger = 0, 0
            for i in range(0, j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_bigger += 1

            right_smaller, right_bigger = 0, 0
            for k in range(j + 1, len(rating)):
                if rating[k] < rating[j]:
                    right_smaller += 1
                else:
                    right_bigger += 1

            res += left_smaller * right_bigger + left_bigger * right_smaller

        return res
