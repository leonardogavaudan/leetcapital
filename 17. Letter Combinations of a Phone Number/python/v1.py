from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = set()
        seen = set()
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def recurse(digits: str, candidate: List[str], mapping: Dict[int, str]):
            if tuple(candidate) in seen:
                return

            if len(candidate) == len(digits):
                res.add("".join(candidate))
                return

            number = int(digits[len(candidate)])
            for c in mapping[number]:
                candidate.append(c)
                recurse(digits, candidate, mapping)
                seen.add(tuple(candidate))
                candidate.pop()

        recurse(digits, [], mapping)
        return list(res)
