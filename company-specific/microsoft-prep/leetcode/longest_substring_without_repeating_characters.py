def lengthOfLongestSubstring(self, s: str) -> int:
    start, end, longest = 0, 0, 0
    seen = set()
    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
        else:
            while s[start] != s[end] and start <= end:
                seen.remove(s[start])
                start += 1
            start += 1
        longest = max(longest, end - start + 1)
        end += 1
    return longest