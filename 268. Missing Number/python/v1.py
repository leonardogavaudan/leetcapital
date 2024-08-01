from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_total = 0
        for num in nums:
            nums_total += num
        return len(nums) * (len(nums) + 1) // 2 - nums_total
