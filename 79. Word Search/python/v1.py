from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(
            board: List[List[str]],
            word: str,
            seen: Set[Tuple[int, int]],
            coords: Tuple[int, int],
        ):
            row, col = coords
            if board[row][col] != word[len(seen)]:
                return False

            seen.add((row, col))
            if len(seen) == len(word):
                return True

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen:
                    if dfs(board, word, seen, (nr, nc)):
                        return True

            seen.remove((row, col))

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(board, word, set(), (row, col)):
                    return True

        return False
