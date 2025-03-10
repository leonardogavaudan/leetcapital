from itertools import islice
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        res = 1
        current_jump = nums[0] - 1
        max_jump = nums[0] - 1

        for num in islice(nums, 1, len(nums) - 1):
            max_jump = max(max_jump, num)

            if current_jump == 0:
                current_jump = max_jump
                res += 1

            current_jump -= 1
            max_jump -= 1

        return res
