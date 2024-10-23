class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()

        def recurse(low: int, high: int):
            nonlocal s, max_length, seen

            if low > high:
                return

            if low == high and s[low] not in "aeiou":
                max_length = max(max_length, 1)
                return

            if max_length >= high - low + 1:
                return

            candidate = s[low : high + 1]
            if candidate in seen:
                return
            seen.add(candidate)

            count = {}

            for i in range(low, high + 1):
                if s[i] not in "aeiou":
                    continue

                if s[i] not in count:
                    count[s[i]] = 0

                count[s[i]] += 1

            for key, value in count.items():
                if value % 2 == 0:
                    continue

                for i in range(low, high + 1):
                    if s[i] == key:
                        recurse(low, i - 1)
                        recurse(i + 1, high)
                return

            max_length = max(max_length, high - low + 1)

        recurse(0, len(s) - 1)

        return max_length
