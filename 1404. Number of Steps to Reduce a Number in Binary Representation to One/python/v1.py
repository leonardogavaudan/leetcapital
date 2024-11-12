class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = s[i]
            if bit == "1":
                if carry == 0:
                    steps += 2
                    carry = 1
                else:
                    steps += 1
            else:
                if carry == 1:
                    steps += 2
                else:
                    steps += 1

        return steps + (carry != 0)
