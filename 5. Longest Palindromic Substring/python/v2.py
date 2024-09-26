class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        largest = s[0]

        for i in range(len(s) - 1):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            current = s[l + 1 : r]
            if len(current) > len(largest):
                largest = current

        for i in range(0, len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            current = s[l + 1 : r]
            if len(current) > len(largest):
                largest = current

        return largest
