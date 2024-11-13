from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        xor_value = 0
        state_to_count = {0: 1}
        state_to_index_sum = {0: 0}

        for k, num in enumerate(arr):
            xor_value ^= num

            if xor_value in state_to_count:
                res += k * state_to_count[xor_value] - state_to_index_sum[xor_value]

            if xor_value not in state_to_count:
                state_to_count[xor_value] = 0
                state_to_index_sum[xor_value] = 0

            state_to_count[xor_value] += 1
            state_to_index_sum[xor_value] += k + 1

        return res
