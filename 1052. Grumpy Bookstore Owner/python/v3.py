from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        total_satisfied = sum(
            customers[i] * (grumpy[i] ^ 1) for i in range(len(customers))
        )
        grumpy_customers = [customers[i] * grumpy[i] for i in range(len(customers))]

        window_count = sum(grumpy_customers[:minutes])
        max_count = window_count

        for i in range(1, len(grumpy_customers) - minutes + 1):
            window_count -= grumpy_customers[i - 1]
            window_count += grumpy_customers[i + minutes - 1]
            max_count = max(max_count, window_count)

        return total_satisfied + max_count
