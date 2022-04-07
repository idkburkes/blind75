class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freqs = dict()
        
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1
        
        for i in range(len(s)):
            if freqs[s[i]] == 1:
                return i
        
        return -1
        