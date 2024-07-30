from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001

        for n in arr1:
            count[n] += 1

        res = []

        for n in arr2:
            res.extend([n] * count[n])
            count[n] = 0

        for n in range(len(count)):
            if count[n] > 0:
                res.extend([n] * count[n])

        return res
