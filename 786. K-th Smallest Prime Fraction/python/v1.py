import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        table = {i: len(arr) - 1 for i in range(len(arr) - 1)}

        heap = []
        for start, end in table.items():
            heapq.heappush(heap, (arr[start] / arr[end], start, end))

        for _ in range(k - 1):
            _, start, end = heapq.heappop(heap)
            if start < end - 1:
                end -= 1
                heapq.heappush(heap, (arr[start] / arr[end], start, end))

        _, start, end = heapq.heappop(heap)

        return [arr[start], arr[end]]
