from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        jump_count = nums[0] - 1
        i = 1
        while i < len(nums) - 1:
            jump_count = max(jump_count, nums[i])
            if jump_count == 0:
                return False

            i += 1
            jump_count -= 1

        return True
