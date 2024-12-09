from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        prefix_to_count = {0: 1}
        for num in nums:
            prefix = (prefix + num) % k
            target = (k - prefix) % k
            res += prefix_to_count.get(target, 0)
            if target not in prefix_to_count:
                prefix_to_count[target] = 0
            prefix_to_count[target] += 1

        return res
