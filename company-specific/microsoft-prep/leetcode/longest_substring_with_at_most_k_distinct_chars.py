class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        res = 0
        seen = dict()
        start = 0
        for end in range(len(s)):
            char = s[end]
            seen[char] = seen.get(char, 0) + 1
            
            while len(seen) > k:
                firstCharInWindow = s[start]
                seen[firstCharInWindow] = seen.get(firstCharInWindow) - 1
                if seen[firstCharInWindow] == 0:
                    del seen[firstCharInWindow]
                start += 1
            
            res = max(res, end - start + 1)
        
        return res
            
                
        
        