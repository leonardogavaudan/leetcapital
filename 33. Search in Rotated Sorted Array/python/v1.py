from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return -1 if target not in nums else nums.index(target)

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
