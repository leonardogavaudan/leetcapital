import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        priority_queue = []

        for start_t, end_t in intervals:
            heapq.heappush(priority_queue, (start_t, 1))
            heapq.heappush(priority_queue, (end_t, -1))

        max_count = 0
        current_count = 0

        while priority_queue:
            current_count += heapq.heappop(priority_queue)[1]
            if current_count > max_count:
                max_count = current_count

        return max_count
