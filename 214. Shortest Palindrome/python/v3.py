class Solution:
    def shortestPalindrome(self, s: str) -> str:
        mod = 10**9 + 1
        base = 29
        power = 1
        prefix = 0
        suffix = 0
        longest_palindrome_len = 0

        for i, c in enumerate(s, 1):
            char_val = ord(c) - ord("a") + 1
            suffix = (suffix * base + char_val) % mod
            prefix = (prefix + char_val * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                longest_palindrome_len = i

        return s[longest_palindrome_len:][::-1] + s
