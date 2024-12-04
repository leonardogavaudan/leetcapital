class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        power = 1
        mod = 10**9 + 7
        largest_palindrome_i = 0

        for i, char in enumerate(s):
            char_val = ord(char) - ord("a") + 1
            suffix = (suffix * base + char_val) % mod
            prefix = (prefix + char_val * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                largest_palindrome_i = i

        return s[largest_palindrome_i + 1 :][::-1] + s
