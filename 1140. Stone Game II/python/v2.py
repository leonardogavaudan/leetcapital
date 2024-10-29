from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def min_max(i: int, alice_turn: bool, m: int) -> int:
            if i >= len(piles):
                return 0

            if (i, alice_turn, m) in memo:
                return memo[(i, alice_turn, m)]

            if alice_turn:
                if i == len(piles) - 1:
                    return piles[i]
                res = -1
                pile_count = 0
                for x in range(1, 2 * m + 1):
                    if i + x > len(piles):
                        break
                    pile_count += piles[i + x - 1]
                    res = max(res, pile_count + min_max(i + x, False, max(m, x)))
                memo[(i, alice_turn, m)] = res
                return res
            else:
                if i == len(piles) - 1:
                    return 0
                res = float("inf")
                for x in range(1, 2 * m + 1):
                    if i + x > len(piles):
                        break
                    res = min(res, min_max(i + x, True, max(m, x)))
                memo[(i, alice_turn, m)] = res
                return int(res)

        return min_max(0, True, 1)
