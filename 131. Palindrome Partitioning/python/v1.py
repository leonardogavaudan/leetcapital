from collections import defaultdict
from typing import List


class Solution:
    def is_palindrome(self, x: List[str]):
        left, right = 0, len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        memo = defaultdict(list)
        res = []

        def recurse(s: str, i: int, partition: List[str]):
            if i == len(s):
                res.append(partition.copy())
                return [[]]

            if memo[i]:
                solutions = [partition + end for end in memo[i]]
                res.extend(solutions)
                return memo[i]

            str_to_add = []
            current_solution_ends = []
            for j in range(i, len(s)):
                str_to_add.append(s[j])
                if self.is_palindrome(str_to_add):
                    partition.append("".join(str_to_add))
                    next_solution_ends = recurse(s, j + 1, partition)
                    if partition:
                        for next_solution_end in next_solution_ends:
                            current_solution_ends.append(
                                [partition[-1]] + next_solution_end
                            )
                    partition.pop()

            memo[i] = current_solution_ends

            return current_solution_ends

        recurse(s, 0, [])

        return res
