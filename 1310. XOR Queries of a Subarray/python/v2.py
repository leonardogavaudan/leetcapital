from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        state = 0
        states = []
        for num in arr:
            state ^= num
            states.append(state)

        res = []

        for left, right in queries:
            xor_res = states[right]
            if left - 1 >= 0:
                xor_res ^= states[left - 1]

            res.append(xor_res)

        return res
