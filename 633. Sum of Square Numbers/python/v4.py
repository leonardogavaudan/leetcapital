class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            b = c - a**2
            if b**0.5 % 1 == 0:
                return True

        return False
