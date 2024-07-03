from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_indices: Dict[int, List[int]] = {}
        for index, value in enumerate(nums):
            if value not in value_to_indices:
                value_to_indices[value] = []
            value_to_indices[value].append(index)

        for value in value_to_indices.keys():
            complement = target - value
            if complement not in value_to_indices:
                continue
            if complement == value:
                if len(value_to_indices[value]) < 2:
                    continue
                else:
                    return [
                        value_to_indices[complement][0],
                        value_to_indices[complement][1],
                    ]
            return [value_to_indices[value][0], value_to_indices[complement][0]]

        raise Exception("problem must have at least 1 solution")
