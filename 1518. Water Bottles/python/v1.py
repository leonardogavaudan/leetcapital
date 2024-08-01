class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        current = numBottles
        while current:
            exchanged = current // numExchange
            if not exchanged:
                break

            res += exchanged
            current = exchanged + current % numExchange

        return res
