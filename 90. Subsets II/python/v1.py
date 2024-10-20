from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        key_to_count = dict(Counter(nums))
        keys = sorted(key_to_count.keys())
        subset = []

        def backtrack(i: int):
            if i == len(keys):
                res.append(subset.copy())
                return

            backtrack(i + 1)

            key = keys[i]
            for count in range(1, key_to_count[key] + 1):
                subset.extend([key] * count)
                backtrack(i + 1)
                subset[-count:] = []

        backtrack(0)
        return res
