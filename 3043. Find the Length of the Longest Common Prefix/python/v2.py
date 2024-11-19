from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for num in arr1:
            if num % 10 == 0:
                seen.add(0)
            while num:
                seen.add(num)
                num //= 10

        res = 0
        for num in arr2:
            stack = []
            while num:
                stack.append(num % 10)
                num //= 10

            i = 0
            while stack:
                num = num * 10 + stack.pop()
                if num not in seen:
                    break
                i += 1
                res = max(res, i)

        return res
