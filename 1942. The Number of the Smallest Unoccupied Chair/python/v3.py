from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        time_heap = []
        arrival_to_departure = {}
        ARRIVAL_CODE = len(times) + 1
        for i, (arrival, departure) in enumerate(times):
            time_heap.append((arrival, ARRIVAL_CODE, i))
            arrival_to_departure[arrival] = departure
        heapq.heapify(time_heap)

        chair_heap = list(range(len(times)))
        heapq.heapify(chair_heap)

        while time_heap:
            time, chair, friend = heapq.heappop(time_heap)
            if friend == targetFriend:
                return heapq.heappop(chair_heap)

            if chair == ARRIVAL_CODE:
                heapq.heappush(
                    time_heap,
                    (arrival_to_departure[time], heapq.heappop(chair_heap), friend),
                )
            else:
                heapq.heappush(chair_heap, chair)

        raise IndexError("Target not found")
