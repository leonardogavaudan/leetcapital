import heapq
import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        res = 0
        arr = [0] * len(nums)
        heap = [(-x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)

        def get_current_val(i):
            return nums[i] + (arr[i] - res) * y

        while heap:
            val, i = heapq.heappop(heap)
            current_val = get_current_val(i)

            if current_val <= 0:
                return res

            steps = max(
                1,
                min(
                    math.ceil(current_val / x),
                    (
                        math.ceil(current_val / x)
                        if not heap or get_current_val(heap[0][1]) <= 0
                        else math.ceil(
                            (current_val - get_current_val(heap[0][1])) / (x - y)
                        )
                    ),
                ),
            )

            heapq.heappush(heap, (val + steps * (x - y), i))
            nums[i] -= x * steps
            arr[i] += steps
            res += steps

        return -1
