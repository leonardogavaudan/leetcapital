class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        latest_char_to_index = {}

        largest = ""
        start_index = 0

        for i, c in enumerate(s):
            if c in latest_char_to_index and latest_char_to_index[c] >= start_index:
                start_index = latest_char_to_index[c] + 1
                latest_char_to_index[c] = i
                continue

            current = s[start_index : i + 1]
            if len(largest) < len(current):
                largest = current

            latest_char_to_index[c] = i

        return len(largest)
