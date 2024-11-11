from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        i = 0
        while i < len(nums) - 1:
            max_jump = max(max_jump, nums[i])
            if max_jump == 0:
                break

            i += 1
            max_jump -= 1

        return i == len(nums) - 1
