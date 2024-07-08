from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_available_spot, second_pointer = 0, 0
        zero_count = 0
        while second_pointer < len(nums):
            if second_pointer == 0:
                second_pointer += 1
                zero_count += 1
            else:
                if next_available_spot != second_pointer:
                    nums[next_available_spot] = nums[second_pointer]
                next_available_spot += 1
                second_pointer += 1
        for i in range(zero_count):
            nums[-(i + 1)] = 0
