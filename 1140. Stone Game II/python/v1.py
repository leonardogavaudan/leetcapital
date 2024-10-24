from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        min_memo = {}
        max_memo = {}

        def min_pile(pile_i: int, m: int) -> int:
            if pile_i + 2 * m >= len(piles):
                min_memo[(pile_i, m)] = 0
                return 0

            if (pile_i, m) in min_memo:
                return min_memo[(pile_i, m)]

            max_results = []
            for x_candidate in range(1, 2 * m + 1):
                max_results.append(max_pile(pile_i + x_candidate, max(x_candidate, m)))

            res = min(max_results)
            min_memo[(pile_i, m)] = res
            return res

        def max_pile(pile_i: int, m: int) -> int:
            if pile_i + 2 * m >= len(piles):
                res = sum(piles[pile_i:])
                max_memo[(pile_i, m)] = res
                return res

            if (pile_i, m) in max_memo:
                return max_memo[(pile_i, m)]

            max_res = 0
            for x_candidate in range(1, 2 * m + 1):
                if pile_i + x_candidate < len(piles):
                    local_piles = sum(piles[pile_i : pile_i + x_candidate])
                    max_res = max(
                        max_res,
                        local_piles
                        + min_pile(pile_i + x_candidate, max(x_candidate, m)),
                    )

            max_memo[(pile_i, m)] = max_res
            return max_res

        return max_pile(0, 1)
