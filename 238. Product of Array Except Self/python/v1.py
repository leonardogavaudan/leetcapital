from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        current_val = 1
        for num in nums:
            current_val *= num
            left.append(current_val)

        right = []
        current_val = 1
        for num in reversed(nums):
            current_val *= num
            right.append(current_val)
        right = right[::-1]

        res = []
        for i in range(len(nums)):
            val = 1
            if i - 1 >= 0:
                val *= left[i - 1]
            if i + 1 < len(nums):
                val *= right[i + 1]
            res.append(val)

        return res
