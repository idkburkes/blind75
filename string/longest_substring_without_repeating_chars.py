class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, longest = 0, 0, 0
        seen = {}
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
            else:
                while s[start] != s[end] and start <= end:
                    del seen[s[start]]
                    start += 1
                start += 1
            longest = max(longest, end - start + 1)
            end += 1
        return longest