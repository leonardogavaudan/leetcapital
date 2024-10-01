from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait_time = 0

        for arrival_time, required_time in customers:
            current_time = max(current_time, arrival_time) + required_time
            total_wait_time += current_time - arrival_time

        return total_wait_time / len(customers)
