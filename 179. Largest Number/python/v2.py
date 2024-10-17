from functools import cmp_to_key
from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1
            if y + x > x + y:
                return 1
            else:
                return 0

        res = list(map(str, nums))
        res.sort(key=cmp_to_key(compare))

        res = "".join(res)

        return "0" if res[0] == "0" else res
