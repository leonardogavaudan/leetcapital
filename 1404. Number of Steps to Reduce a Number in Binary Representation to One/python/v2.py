class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        remainder = 0
        for i in range(len(s) - 1, 0, -1):
            digit = s[i]
            if digit == "0":
                res += 1 + int(remainder == 1)
            elif digit == "1":
                res += 1 + int(remainder == 0)
                remainder = 1

        res += int(remainder == 1)

        return res
