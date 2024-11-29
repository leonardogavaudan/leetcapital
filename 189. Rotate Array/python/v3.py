from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr: List[int], left: int, right: int):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
