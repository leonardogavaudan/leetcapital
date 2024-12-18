from typing import Dict, List, Tuple


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def recurse(
            expression: str,
            start: int,
            end: int,
            memo: Dict[Tuple[int, int], List[int]],
        ) -> List[int]:
            if (start, end) in memo:
                return memo[start, end]

            if end - start < 2:
                return [int(expression[start : end + 1])]

            res = []
            for i in range(start, end + 1):
                if expression[i].isdigit():
                    continue

                left = recurse(expression, start, i - 1, memo)
                right = recurse(expression, i + 1, end, memo)

                for r in right:
                    for l in left:
                        if expression[i] == "+":
                            res.append(l + r)
                        elif expression[i] == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)

            memo[(start, end)] = res
            return res

        return recurse(expression, 0, len(expression) - 1, memo)
