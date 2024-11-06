from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        i = 0
        length = 0
        max_length = 0
        while i < len(nums):
            if nums[i] != max_val:
                length = 0
            else:
                length += 1
                max_length = max(max_length, length)

            i += 1

        return max_length
