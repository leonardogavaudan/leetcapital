from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                total += 1

        return total

