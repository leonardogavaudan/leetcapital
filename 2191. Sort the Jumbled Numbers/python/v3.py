from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_num(mapping: List[int], num: int):
            if num == 0:
                return mapping[0]
            res = 0
            power = 0
            while num:
                res = res + mapping[num % 10] * 10**power
                power += 1
                num //= 10
            return res

        nums.sort(key=lambda x: map_num(mapping, x))
        return nums
