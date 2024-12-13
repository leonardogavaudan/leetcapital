from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]

        def is_palindrome(arr: List[str]):
            left, right = 0, len(arr) - 1
            while left < right:
                if arr[left] != arr[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(len(s) - 1, -1, -1):
            prefix_candidate = []
            for j in range(i, len(s)):
                prefix_candidate.append(s[j])
                if is_palindrome(prefix_candidate):
                    for prev_palindromes in dp[j + 1]:
                        dp[i].append(["".join(prefix_candidate)] + prev_palindromes)

        return dp[0]
