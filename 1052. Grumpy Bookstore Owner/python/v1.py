from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        if len(customers) < minutes:
            return sum(customers)

        total_satisified = sum((c * (g ^ 1) for c, g in zip(customers, grumpy)))
        max_window = sum((c * g for c, g in zip(customers[:minutes], grumpy[:minutes])))
        current_window = max_window
        for i in range(1, len(customers) - (minutes - 1)):
            current_window -= customers[i - 1] * grumpy[i - 1]
            current_window += customers[i + (minutes - 1)] * grumpy[i + (minutes - 1)]
            max_window = max(max_window, current_window)

        return total_satisified + max_window
