from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        max_count = 0
        count = 0

        for num in nums:
            if num > max_val:
                max_val = num
                count = 1
                max_count = 1
            elif num == max_val:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count
