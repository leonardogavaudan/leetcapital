class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        for c in s[slice(len(s) - 1, 0, -1)]:
            digit = int(c)
            if digit == 0:
                if carry == 0:
                    res += 1
                else:
                    res += 2
            else:
                if carry == 0:
                    res += 2
                    carry = 1
                else:
                    res += 1

        return res + carry
