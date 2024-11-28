class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        opening_bracket_count = 0
        for c in s:
            if c == "[":
                opening_bracket_count += 1
            else:
                if opening_bracket_count:
                    opening_bracket_count -= 1
                else:
                    res += 1

        return res
