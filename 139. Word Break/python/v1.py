from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wd = set(wordDict)

        def recurse(s: str, start: int, end: int, wd: set, memo: dict):
            if (start, end) in memo:
                return memo[(start, end)]

            if start > end:
                return True

            for i in range(start, end + 1):
                if s[start : i + 1] in wd and recurse(s, i + 1, end, wd, memo):
                    memo[(start, end)] = True
                    return True

            memo[(start, end)] = False
            return False

        return recurse(s, 0, len(s) - 1, wd, memo)
