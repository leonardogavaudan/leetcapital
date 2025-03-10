from itertools import islice
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for num in islice(nums, 0, len(nums) - 1):
            max_jump = max(max_jump, num)
            if max_jump == 0:
                return False
            max_jump -= 1

        return True
