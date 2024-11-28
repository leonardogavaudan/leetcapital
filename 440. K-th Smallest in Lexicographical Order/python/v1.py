class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int):
            current = prefix
            next_prefix = prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        k = k - 1
        current = 1
        while k:
            count = count_prefix(current, n)
            if count <= k:
                k -= count
                current += 1
            else:
                k -= 1
                current *= 10

        return current
