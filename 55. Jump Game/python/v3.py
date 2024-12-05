from itertools import islice
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        jump = 0
        for num in islice(nums, 0, len(nums) - 1):
            jump = max(jump, num)
            jump -= 1
            if jump == -1:
                return False

        return True
