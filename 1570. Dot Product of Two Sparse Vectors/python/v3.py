from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.key_to_val = {}
        for i, num in enumerate(nums):
            if num:
                self.key_to_val[i] = num

    def dotProduct(self, vec: "SparseVector") -> int:
        sparse_keys = min(self, vec, key=lambda x: len(x.key_to_val)).key_to_val.keys()
        return sum(
            (
                self.key_to_val.get(key, 0) * vec.key_to_val.get(key, 0)
                for key in sparse_keys
            )
        )
