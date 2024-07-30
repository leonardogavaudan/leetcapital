from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_len = len(nums)
        i, j = 1, 1
        prev_value = nums[0]

        while j < len(nums):
            if nums[j] == prev_value:
                j += 1
                new_len -= 1
            else:
                prev_value = nums[j]
                nums[i] = nums[j]
                j += 1
                i += 1

        return new_len
