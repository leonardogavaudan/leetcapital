class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(n: int, n1: int, n2: int):
            count = 0
            c1 = n1
            c2 = n2
            while c1 <= n:
                count += min(n + 1, c2) - c1
                c1 *= 10
                c2 *= 10
            return count

        curr = 1
        k -= 1
        while k > 0:
            steps = count(n, curr, curr + 1)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr
