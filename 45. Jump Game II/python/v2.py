from itertools import islice
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_reach = potential_reach = nums[0]

        for num in islice(nums, 1, len(nums) - 1):
            current_reach -= 1
            potential_reach -= 1

            potential_reach = max(potential_reach, num)

            if current_reach == 0:
                jumps += 1
                current_reach = potential_reach

        jumps += 1

        return jumps
