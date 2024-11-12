from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        res = 0

        for num in arr1:
            digits_reversed = []
            while num:
                digits_reversed.append(num % 10)
                num //= 10
            prefix = []
            for digit in reversed(digits_reversed):
                prefix.append(digit)
                seen.add(tuple(prefix))

        for num in arr2:
            digits_reversed = []
            while num:
                digits_reversed.append(num % 10)
                num //= 10
            if len(digits_reversed) <= res:
                continue

            target = []
            for digit in reversed(digits_reversed):
                target.append(digit)
                if tuple(target) not in seen:
                    break
                res = max(res, len(target))

        return res
