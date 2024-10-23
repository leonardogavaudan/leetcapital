class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        i, j = 0, int(c**0.5)

        while i <= j:
            candidate = i**2 + j**2
            if candidate == c:
                return True
            elif candidate < c:
                i += 1
            else:
                j -= 1

        return False
