from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def min_max(i: int, m: int, is_alice_turn: bool):
            nonlocal piles

            if i >= len(piles):
                return 0

            if (i, m, is_alice_turn) in memo:
                return memo[(i, m, is_alice_turn)]

            if is_alice_turn:
                if 2 * m + i - 1 >= len(piles) - 1:
                    return sum(piles[i:])
                max_res = 0
                piles_count = 0
                for j in range(1, 2 * m + 1):
                    piles_count += piles[i + j - 1]
                    min_max_result = min_max(i + j, max(m, 2 * j), False)
                    max_res = max(max_res, piles_count + min_max_result)
                memo[(i, m, is_alice_turn)] = max_res
                return max_res
            else:
                if 2 * m + i - 1 >= len(piles) - 1:
                    return 0
                min_res = 2**15 - 1
                for j in range(1, 2 * m + 1):
                    min_max_result = min_max(i + j, max(m, 2 * j), True)
                    min_res = min(min_res, min_max_result)
                memo[(i, m, is_alice_turn)] = min_res
                return min_res

        return min_max(0, 1, True)
