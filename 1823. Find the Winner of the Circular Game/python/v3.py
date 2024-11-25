class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_index = 0
        for size in range(2, n + 1):
            winner_index = (winner_index + k) % size

        return winner_index + 1
