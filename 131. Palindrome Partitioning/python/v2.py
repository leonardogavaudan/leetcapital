from typing import List


class Solution:
    def is_palindrome(self, s: List[str]):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            candidate = []
            for j in range(i, len(s)):
                candidate.append(s[j])
                if self.is_palindrome(candidate):
                    palindrome = "".join(candidate)
                    for previous_solution in dp[j + 1]:
                        dp[i].append([palindrome] + previous_solution)
        return dp[0]
