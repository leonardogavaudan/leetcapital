from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for course, pre_req in prerequisites:
            graph[pre_req].append(course)
            in_degree[course] += 1

        queue = deque([c for c in range(numCourses) if in_degree[c] == 0])
        visited_count = 0
        while queue:
            current = queue.popleft()
            visited_count += 1

            for nxt in graph[current]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        return visited_count == numCourses
