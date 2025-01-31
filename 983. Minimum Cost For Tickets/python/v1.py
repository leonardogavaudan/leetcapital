from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        days_set = set(days)

        def recurse(day: int, current_cost: int, days_left: int):
            memo_key = (day, current_cost, days_left)
            if memo_key in memo:
                return memo

            if day == 0:
                return 0

            res = float("inf")
            if day not in days_set or days_left > 0:
                res = recurse(day - 1, current_cost, days_left - 1)
            else:
                for cost, day_pass in zip(costs, [1, 7, 30]):
                    res = min(day - 1, current_cost + cost, day_pass - 1)

            memo[memo_key] = res
            return res

        return recurse(max(days), 0, 0)
