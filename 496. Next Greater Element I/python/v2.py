from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack_values = []
        value_to_next_greater_value = {}
        for i, num in enumerate(nums2):
            while len(stack_values) > 0 and stack_values[-1] < num:
                value_to_next_greater_value[stack_values.pop()] = num

            stack_values.append(num)

        res = []
        for num in nums1:
            if num in value_to_next_greater_value:
                res.append(value_to_next_greater_value[num])
            else:
                res.append(-1)

        return res
