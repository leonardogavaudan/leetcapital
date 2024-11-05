class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(1, n):
            res = (res + k) % (i + 1)
        return res + 1
