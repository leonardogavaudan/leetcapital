from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        memo = {}
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def recurse(digits: str, i: int, memo: dict, mapping: dict):
            if i in memo:
                return memo[i]

            if i >= len(digits):
                return [""]

            res = []
            for c in mapping[digits[i]]:
                recurse_res = recurse(digits, i + 1, memo, mapping)
                for r in recurse_res:
                    res.append(c + r)

            memo[i] = res
            return res

        return recurse(digits, 0, memo, mapping)
