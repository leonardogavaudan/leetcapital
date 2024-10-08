class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = 0
        count_b = 0

        seen_a = False
        seen_b = False

        i, j = 0, len(s) - 1

        while i < len(s) and j >= 0:
            if s[i] == "b":
                seen_b = True
            if s[j] == "a":
                seen_a = True

            if seen_b and s[i] == "a":
                count_a += 1
            if seen_a and s[j] == "b":
                count_b += 1

            i += 1
            j -= 1

        l, r = 0, len(s) - 1

        while l < len(s) and s[l] != "b":
            l += 1
        while r >= 0 and s[r] != "a":
            r -= 1

        deletion_count = 0

        while l < r:
            if count_a > count_b:
                count_b -= 1
                l += 1
                while l < r and s[l] != "b":
                    count_a -= 1
                    l += 1
            else:
                count_a -= 1
                r -= 1
                while l < r and s[r] != "a":
                    count_b -= 1
                    r -= 1

            deletion_count += 1

        return deletion_count
