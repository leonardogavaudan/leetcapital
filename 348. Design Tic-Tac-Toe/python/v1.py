from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diagonal_we = 0
        self.diagonal_ew = 0

    def move(self, row: int, col: int, player: int) -> int:
        point_change = 1 if player == 1 else -1

        self.rows[row] += point_change
        self.cols[col] += point_change

        if row == col:
            self.diagonal_we += point_change
        if row == self.n - col:
            self.diagonal_ew += point_change

        if point_change * self.n in [
            self.rows[row],
            self.cols[col],
            self.diagonal_we,
            self.diagonal_ew,
        ]:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
