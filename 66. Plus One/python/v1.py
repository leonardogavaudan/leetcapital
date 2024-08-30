from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                carry = 0
                break

            digits[i] = 0
            i -= 1

        if carry == 1:
            digits = [1] + digits

        return digits
