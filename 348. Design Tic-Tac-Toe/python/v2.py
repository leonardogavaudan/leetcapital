from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diagonal_ew = 0
        self.diagonal_we = 0

    def move(self, row: int, col: int, player: int) -> int:
        point_change = 1 if player == 1 else -1
        self.rows[row] += point_change
        self.cols[col] += point_change
        if row == col:
            self.diagonal_ew += point_change
        if row + col == self.n - 1:
            self.diagonal_we += point_change

        if self.n in map(
            abs,
            [
                self.rows[row],
                self.cols[col],
                self.diagonal_ew,
                self.diagonal_we,
            ],
        ):
            return player
        else:
            return 0
