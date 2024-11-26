from typing import List


class Solution:
    def is_palindrome(self, x: List[str]):
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]

        for i in range(len(s) - 1, -1, -1):
            candidate = []
            for j in range(i, len(s)):
                candidate.append(s[j])
                if self.is_palindrome(candidate):
                    for solution in dp[j + 1]:
                        dp[i].append(["".join(candidate)] + solution)

        return dp[0]
