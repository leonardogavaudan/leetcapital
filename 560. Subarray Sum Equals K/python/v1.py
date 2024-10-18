from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hash_cum = defaultdict(int)
        hash_cum[0] = 1
        cum_sum = 0

        for num in nums:
            cum_sum += num
            if cum_sum - k in hash_cum:
                res += hash_cum[cum_sum - k]

            hash_cum[cum_sum] += 1

        return res
