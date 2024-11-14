from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.pos_to_val = {}
        for i, num in enumerate(nums):
            if num:
                self.pos_to_val[i] = num

    def dotProduct(self, vec: "SparseVector") -> int:
        total = 0
        keys = (
            self.pos_to_val.keys()
            if len(self.pos_to_val) < len(vec.pos_to_val)
            else vec.pos_to_val.keys()
        )
        for key in keys:
            total += self.pos_to_val.get(key, 0) * vec.pos_to_val.get(key, 0)
        return total
