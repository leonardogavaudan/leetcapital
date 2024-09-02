from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_value_to_index = {}
        for i, num in enumerate(nums2):
            nums2_value_to_index[num] = i

        nums2_max_value_seen_from_index = {}
        max_value = 0
        for i in range(len(nums2) - 1, -1, -1):
            if nums2[i] > max_value:
                max_value = nums2[i]
            nums2_max_value_seen_from_index[i] = max_value 

        res = []

        for num in nums1:
            index = nums2_value_to_index[num]
            if index == len(nums2) - 1 or nums2_max_value_seen_from_index[index + 1] <= num:
                res.append(-1)
            else:
                for i in range(index + 1, len(nums2)):
                    if nums2[i] > num:
                        res.append(nums2[i])
                        break

        return res
