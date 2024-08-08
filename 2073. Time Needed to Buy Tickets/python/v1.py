from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0

        for i, ticket in enumerate(tickets):
            if ticket < tickets[k]:
                total += ticket
            else:
                total += tickets[k]
                if i > k:
                    total -= 1

        return total
