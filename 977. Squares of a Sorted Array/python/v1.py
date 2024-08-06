from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        p1 = 0
        while p1 < len(nums) and nums[p1] < 0:
            p1 += 1

        p2 = p1 - 1

        while p2 >= 0 and p1 < len(nums):
            if abs(nums[p1]) <= abs(nums[p2]):
                res.append(nums[p1] ** 2)
                p1 += 1
            else:
                res.append(nums[p2] ** 2)
                p2 -= 1

        while p1 < len(nums):
            res.append(nums[p1] ** 2)
            p1 += 1

        while p2 >= 0:
            res.append(nums[p2] ** 2)
            p2 -= 1

        return res
