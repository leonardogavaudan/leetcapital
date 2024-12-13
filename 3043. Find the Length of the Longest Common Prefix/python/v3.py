from typing import List
import math


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def generate_prefixes(num: int):
            prefixes = []
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            digits = digits[::-1]

            prefix = 0
            for digit in digits:
                prefix = 10 * prefix + digit
                prefixes.append(prefix)
            return prefixes

        prefix_set1 = set()
        for num in arr1:
            prefix_set1.update(generate_prefixes(num))

        prefix_set2 = set()
        for num in arr2:
            prefix_set2.update(generate_prefixes(num))

        if not (prefix_set1 & prefix_set2):
            return 0

        max_value = max(prefix_set1 & prefix_set2)
        return math.floor(math.log(max_value, 10)) + 1
