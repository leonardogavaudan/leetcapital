from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum_to_index = {0: -1}
        sum = 0

        for i, num in enumerate(nums):
            sum = (sum + num) % k
            if sum in prefix_sum_to_index:
                if i - prefix_sum_to_index[sum] >= 2:
                    return True
            else:
                prefix_sum_to_index[sum] = i

        return False
