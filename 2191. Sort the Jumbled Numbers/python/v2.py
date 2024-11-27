from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        to_mapping = {i: value for i, value in enumerate(mapping)}

        def map_to_new(num: int) -> int:
            nonlocal to_mapping
            if num == 0:
                return to_mapping[0]

            res = 0
            i = 0
            while num:
                res += to_mapping[(num % 10)] * 10**i
                num //= 10
                i += 1
            return res

        return list(
            map(
                lambda x: nums[x[1]],
                sorted([(map_to_new(value), i) for i, value in enumerate(nums)]),
            )
        )
