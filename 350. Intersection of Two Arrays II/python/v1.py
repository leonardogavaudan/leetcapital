from typing import Counter, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_to_count = Counter(nums1)

        res = []

        for num in nums2:
            if num in nums1_to_count:
                res.append(num)
                nums1_to_count[num] -= 1
                if nums1_to_count[num] == 0:
                    del nums1_to_count[num]

        return res
