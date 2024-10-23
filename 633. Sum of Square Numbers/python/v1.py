class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        seen = set()
        for x in range(int(c**0.5) + 1):
            seen.add(x**2)
            target = c - x**2

            if target in seen:
                return True

        return False
