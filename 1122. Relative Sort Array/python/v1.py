from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        number_to_count = {}

        for k in arr1:
            if k not in number_to_count:
                number_to_count[k] = 0
            number_to_count[k] += 1

        res = []

        for k in arr2:
            while number_to_count[k]:
                res.append(k)
                number_to_count[k] -= 1
            del number_to_count[k]

        rest_array = []
        for number, count in number_to_count.items():
            for _ in range(count):
                rest_array.append(number)

        rest_array.sort()
        for k in range(len(rest_array)):
            res.append(rest_array[k])

        return res
