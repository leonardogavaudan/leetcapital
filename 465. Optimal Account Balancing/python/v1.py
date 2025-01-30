from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        net = defaultdict(int)
        for fr, to, amount in transactions:
            net[fr] += amount
            net[to] -= amount

        balances = [balance for balance in net.values() if balance != 0]

        def backtrack(start: int):
            while start < len(balances) and balances[start] == 0:
                start += 1

            if start == len(balances):
                return 0

            res = float("inf")
            for i in range(start + 1, len(balances)):
                if balances[start] * balances[i] >= 0:
                    continue

                original_i = balances[i]
                balances[i] += balances[start]
                res = min(res, 1 + backtrack(start + 1))
                balances[i] = original_i

            return res

        return backtrack(0)
