from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_to_count = defaultdict(int)
        sum_to_count[nums[0]] += 1
        sum_to_count[-nums[0]] += 1

        for i in range(1, len(nums)):
            new_sum_to_count = defaultdict(int)
            for curr_sum, count in sum_to_count.items():
                for new_sum in [curr_sum + nums[i], curr_sum - nums[i]]:
                    new_sum_to_count[new_sum] += count

            sum_to_count = new_sum_to_count

        return sum_to_count.get(target, 0)
