class Solution:
    def shortestPalindrome(self, s: str) -> str:
        suffix = 0
        prefix = 0
        base = 29
        power = 1
        largest_palindrome_length = 0
        mod = 10**9 + 7

        for i, c in enumerate(s):
            char_val = ord(c) - ord("a") + 1
            prefix = (prefix * base + char_val) % mod
            suffix = (suffix + char_val * power) % mod
            power = (power * base) % mod
            if prefix == suffix:
                largest_palindrome_length = i

        return s[largest_palindrome_length + 1 :][::-1] + s
