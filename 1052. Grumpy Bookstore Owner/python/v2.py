from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        if len(customers) == minutes:
            return sum(customers)

        happy_customers_count = sum(
            (customers[i] * (grumpy[i] ^ 1) for i in range(len(customers)))
        )
        window = sum((customers[i] * grumpy[i] for i in range(minutes)))
        max_window = window
        for i in range(1, len(customers) - minutes + 1):
            window = (
                window
                - customers[i - 1] * grumpy[i - 1]
                + customers[i + minutes - 1] * grumpy[i + minutes - 1]
            )
            max_window = max(max_window, window)

        return happy_customers_count + max_window
