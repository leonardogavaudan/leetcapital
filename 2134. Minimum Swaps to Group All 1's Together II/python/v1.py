from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size = 0
        for num in nums:
            if num == 1:
                window_size += 1

        if window_size == len(nums):
            return 0

        current_count = 0
        i, j = 0, 0
        while i < window_size:
            current_count += nums[i]
            i += 1

        i -= 1
        max_count = current_count

        while j < len(nums):
            if current_count > max_count:
                max_count = current_count

            i += 1
            i_index = i % len(nums)
            current_count += nums[i_index]

            current_count -= nums[j]
            j += 1

        return window_size - max_count
