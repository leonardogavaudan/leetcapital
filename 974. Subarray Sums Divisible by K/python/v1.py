from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_to_count = {0: 1}
        prefix = 0

        for num in nums:
            prefix = (prefix + num) % k
            if prefix in prefix_to_count:
                res += prefix_to_count[prefix]
            else:
                prefix_to_count[prefix] = 0

            prefix_to_count[prefix] += 1

        return res
