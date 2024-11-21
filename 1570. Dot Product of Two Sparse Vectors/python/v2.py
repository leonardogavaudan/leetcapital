from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i, num in enumerate(nums):
            if num:
                self.values[i] = num

    def dotProduct(self, vec: "SparseVector") -> int:
        keys = (
            self.values.keys()
            if len(self.values) < len(vec.values)
            else vec.values.keys()
        )

        res = 0
        for key in keys:
            res += self.values.get(key, 0) * vec.values.get(key, 0)

        return res
