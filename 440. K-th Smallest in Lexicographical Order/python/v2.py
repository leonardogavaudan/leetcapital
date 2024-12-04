class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix: int, n: int):
            count = 0
            initial_prefix = prefix
            next_prefix = initial_prefix + 1
            while initial_prefix <= n:
                count += min(next_prefix, n + 1) - initial_prefix
                initial_prefix *= 10
                next_prefix *= 10
            return count

        k -= 1
        prefix = 1
        while k:
            count = get_count(prefix, n)
            if count <= k:
                prefix += 1
                k -= count
            else:
                prefix *= 10
                k -= 1
        return prefix
