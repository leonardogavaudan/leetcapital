from typing import List
import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs_heap = []
        for i in range(len(times)):
            heapq.heappush(chairs_heap, i)

        events_heap = []
        arrival_to_leaving = {}
        for i, (arrival, leaving) in enumerate(times):
            heapq.heappush(events_heap, (arrival, len(times) + 1, i))
            arrival_to_leaving[arrival] = leaving

        while events_heap:
            event_time, event_chair, i = heapq.heappop(events_heap)
            if event_chair != len(times) + 1:
                heapq.heappush(chairs_heap, event_chair)
            else:
                chair = heapq.heappop(chairs_heap)
                if i == targetFriend:
                    return chair
                leaving = arrival_to_leaving[event_time]
                heapq.heappush(events_heap, (leaving, chair, i))

        raise IndexError()
