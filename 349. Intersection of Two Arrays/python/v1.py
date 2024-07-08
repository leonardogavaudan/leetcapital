from typing import Dict, List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        int_to_count: Dict[int, int] = {}
        for num in nums1:
            if num not in int_to_count:
                int_to_count[num] = 1

        for num in nums2:
            if num in int_to_count:
                int_to_count[num] = 2

        return [num for num, count in int_to_count.items() if count == 2]
