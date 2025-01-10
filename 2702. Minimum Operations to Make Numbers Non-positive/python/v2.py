import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def f(R: int):
            total = 0
            for num in nums:
                required = num - R * y
                if required > 0:
                    total += math.ceil(required / (x - y))

                    if total > R:
                        return total

            return total

        left, right = 0, 2 * 10**9
        while left <= right:
            mid = (left + right) // 2
            if f(mid) <= mid:
                right = mid - 1
            else:
                left = mid + 1

        return left
