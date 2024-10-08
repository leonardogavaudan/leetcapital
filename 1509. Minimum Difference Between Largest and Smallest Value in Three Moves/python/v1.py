from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        min_diff = float("inf")

        def recurse(l: int, r: int, move: int) -> None:
            if move > 3:
                return

            nonlocal min_diff

            if l == r:
                min_diff = 0
                return

            diff = sorted_nums[r] - sorted_nums[l]
            if diff < min_diff:
                min_diff = diff

            recurse(l + 1, r, move + 1)
            recurse(l, r - 1, move + 1)

        recurse(0, len(sorted_nums) - 1, 0)

        return int(min_diff)
