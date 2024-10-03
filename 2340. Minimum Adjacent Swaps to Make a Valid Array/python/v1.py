from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min, max = float("inf"), float("-inf")

        for num in nums:
            if num < min:
                min = num
            if num > max:
                max = num

        left_swap_count = 0
        while left_swap_count < len(nums):
            if nums[left_swap_count] == min:
                break
            left_swap_count += 1

        right_swap_count = len(nums) - 1
        while right_swap_count >= 0:
            if nums[right_swap_count] == max:
                break
            right_swap_count -= 1

        right_swap_count = len(nums) - 1 - right_swap_count

        if left_swap_count + right_swap_count >= len(nums):
            return left_swap_count + right_swap_count - 1
        else:
            return left_swap_count + right_swap_count
