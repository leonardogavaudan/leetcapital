class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(1, n):
            winner = (winner + k) % (i + 1)
        return winner + 1
