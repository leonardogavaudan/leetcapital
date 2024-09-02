from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_to_count = {
                5: 0,
                10: 0,
        }

        for bill in bills:
            difference = bill - 5 

            if bill == 20 and  bill_to_count[10] > 0:
                bill_to_count[10] -= 1
                difference -= 10

            while difference != 0:
                if bill_to_count[5] == 0:
                    return False

                bill_to_count[5] -= 1
                difference -= 5

            if bill != 20:
                bill_to_count[bill] += 1

        return True
