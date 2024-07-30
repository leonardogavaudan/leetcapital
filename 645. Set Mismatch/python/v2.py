from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x_or_all = 0

        for k in range(1, len(nums) + 1):
            x_or_all ^= k

        for k in nums:
            x_or_all ^= k

        x_or_all_right_most_set_bit = x_or_all & -x_or_all

        x_or_not_set = 0
        x_or_set = 0

        for i in range(1, len(nums) + 1):
            if x_or_all_right_most_set_bit & i:
                x_or_set ^= i
            else:
                x_or_not_set ^= i

        for n in nums:
            if x_or_all_right_most_set_bit & n:
                x_or_set ^= n
            else:
                x_or_not_set ^= n

        for i in nums:
            if i == x_or_not_set:
                return [x_or_not_set, x_or_set]

        return [x_or_set, x_or_not_set]
