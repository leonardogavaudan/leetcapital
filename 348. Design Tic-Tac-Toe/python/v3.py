from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.we_diagonal = 0
        self.ew_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        point_change = 1 if player == 1 else -1

        self.rows[row] += point_change
        self.cols[col] += point_change
        if row == col:
            self.we_diagonal += point_change
        if row + col == self.n - 1:
            self.ew_diagonal += point_change

        if self.n in map(
            abs,
            [
                self.rows[row],
                self.cols[col],
                self.we_diagonal,
                self.ew_diagonal,
            ],
        ):
            return player

        return 0
