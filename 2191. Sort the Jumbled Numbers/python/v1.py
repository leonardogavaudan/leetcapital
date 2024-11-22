from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            new_mapping = 0 if num else mapping[0]
            j = 0
            while num:
                new_mapping += (mapping[num % 10]) * 10**j
                j += 1
                num //= 10
            res.append((i, new_mapping))

        res.sort(key=lambda x: x[1])
        return [nums[key] for key, _ in res]
