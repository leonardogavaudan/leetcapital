from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            while 0 < i < len(nums) - 1 and nums[i - 1] == nums[i]:
                i += 1

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif current_sum < 0:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
            i += 1

        return res
