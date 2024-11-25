class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        remainder = 0

        for i in range(len(s) - 1, 0, -1):
            if s[i] == "0":
                if remainder == 0:
                    res += 1
                else:
                    res += 2
            else:
                if remainder == 0:
                    res += 2
                    remainder = 1
                else:
                    res += 1

        return res + remainder
