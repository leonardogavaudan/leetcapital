class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(n):
            temp = y
            y += x
            x = temp
            n += 1

        return y
