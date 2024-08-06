from typing import List
import heapq


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        MAX_ID = 1000
        score_map = {}
        id_used = [False] * MAX_ID

        for id, score in items:
            if id not in score_map:
                score_map[id] = []

            if len(score_map[id]) < 5:
                heapq.heappush(score_map[id], score)
            elif score > score_map[id][0]:
                heapq.heapreplace(score_map[id], score)

            id_used[id - 1] = True

        res = []
        for id in range(1, MAX_ID + 1):
            if id_used[id - 1]:
                avg_score = sum(score_map[id]) // 5
                res.append([id, avg_score])

        return res
