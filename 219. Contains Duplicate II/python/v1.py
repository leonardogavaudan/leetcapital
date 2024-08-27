from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_to_indices: Dict[int, List[int]] = {}

        for index, value in enumerate(nums):
            if value not in value_to_indices:
                value_to_indices[value] = []
            value_to_indices[value].append(index)

        for value, indices in value_to_indices.items():
            if len(indices) < 2:
                continue

            i = 0
            while i < len(indices) - 1:
                if indices[i + 1] - indices[i] <= k:
                    return True

        return False
