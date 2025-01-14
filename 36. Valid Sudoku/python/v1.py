from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        row_to_nums = [set(range(1, 10)) for _ in range(N)]
        col_to_nums = [set(range(1, 10)) for _ in range(N)]
        squares = [[set(range(1, 10)) for _ in range(3)] for _ in range(3)]

        for r in range(N):
            for c in range(N):
                if not board[r][c].isdigit():
                    continue

                relevant_sets = [
                    row_to_nums[r],
                    col_to_nums[c],
                    squares[r // 3][c // 3],
                ]

                for s in relevant_sets:
                    if int(board[r][c]) not in s:
                        return False
                    else:
                        s.remove(int(board[r][c]))

        return True
