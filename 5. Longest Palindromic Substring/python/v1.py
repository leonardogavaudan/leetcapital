from typing import List


class Solution:
    def generate_all_substrings(self, s: str) -> List[str]:
        res = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                res.append(s[i:j])

        return res

    def is_palindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def longestPalindrome(self, s: str) -> str:
        substrings = self.generate_all_substrings(s)
        substrings.sort(key=len, reverse=True)
        for substring in substrings:
            if self.is_palindrome(substring):
                return substring

        return ""
