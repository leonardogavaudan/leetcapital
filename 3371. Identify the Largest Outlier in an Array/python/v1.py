from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        nums.sort()

        for i in range(len(nums) - 1, -1, -1):
            total_without_outlier = total - nums[i]
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                target = total_without_outlier - nums[mid]
                if nums[mid] == target:
                    if mid != i:
                        return nums[i]
                    if i - 1 > -1 and nums[i - 1] == nums[i]:
                        return nums[i]
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        raise AssertionError("Solution not found")
