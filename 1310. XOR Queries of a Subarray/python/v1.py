from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []

        prefix_xor = [0]
        xor = 0
        for num in arr:
            xor ^= num
            prefix_xor.append(xor)

        for left, right in queries:
            res.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return res
