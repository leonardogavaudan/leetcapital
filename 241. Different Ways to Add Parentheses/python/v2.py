from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def recurse(s: str):
            if s.isdigit():
                return [int(s)]

            results = []
            for i, c in enumerate(s):
                if c in "+-*":
                    left_results = recurse(s[:i])
                    right_results = recurse(s[i + 1 :])

                    for left in left_results:
                        for right in right_results:
                            if c == "+":
                                results.append(left + right)
                            if c == "-":
                                results.append(left - right)
                            if c == "*":
                                results.append(left * right)

            return results

        return recurse(expression)
