class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        opening_count = 0
        for c in s:
            if c == "(":
                opening_count += 1
            if c == ")":
                if opening_count:
                    opening_count -= 1
                else:
                    res += 1

        return res + opening_count
