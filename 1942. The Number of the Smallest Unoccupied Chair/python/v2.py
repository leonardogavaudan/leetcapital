import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs_heap = []
        for i in range(len(times)):
            heapq.heappush(chairs_heap, i)

        events_heap = []
        arrival_to_departure = {}
        for friend_i, (arrival, departure) in enumerate(times):
            heapq.heappush(events_heap, (arrival, len(times) + 1, friend_i))
            arrival_to_departure[arrival] = departure

        while events_heap:
            time, chair_i, friend_i = heapq.heappop(events_heap)
            if chair_i == len(times) + 1:
                chair = heapq.heappop(chairs_heap)
                if friend_i == targetFriend:
                    return chair
                departure = arrival_to_departure[time]
                heapq.heappush(events_heap, (departure, chair, friend_i))
            else:
                heapq.heappush(chairs_heap, chair_i)

        return -1
