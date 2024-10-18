from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []

        def dfs(total: int, i: int):
            nonlocal candidates
            if total > target or i >= len(candidates):
                return

            if total == target:
                res.append(candidate.copy())
                return

            candidate.append(candidates[i])
            dfs(total + candidates[i], i)

            candidate.pop()
            dfs(total, i + 1)

        dfs(0, 0)

        return res
