from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = []
        xor = 0
        for num in arr:
            xor ^= num
            prefix_xor.append(xor)

        return [
            prefix_xor[right] ^ (prefix_xor[left - 1] if left - 1 >= 0 else 0)
            for left, right in queries
        ]
