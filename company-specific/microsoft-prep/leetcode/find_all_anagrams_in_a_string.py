class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # pattern is longer than string so there are no anagrams
        if len(p) > len(s):
            return []

        # represent freq count with array, can be compared in O(1) time
        map_p = [0 for _ in range(26)]
        map_s = [0 for _ in range(26)]
        
        # populate the target map
        for c in p:
            idx = ord(c) - ord('a')
            map_p[idx] += 1
            
        start = end = 0
        
        # create first window
        while end < len(p):
            idx = ord(s[end]) - ord('a')
            map_s[idx] += 1
            end += 1
        
        res = []
        
        # start sliding window
        while end < len(s):
            if map_s == map_p:
                res.append(start)
                
            #add last char
            idx = ord(s[end]) - ord('a')
            map_s[idx] += 1
            end += 1
            
            #remove first char
            idx = ord(s[start]) - ord('a')
            map_s[idx] -= 1
            start += 1
            
        # check if last window was valid anagram
        if map_s == map_p:
            res.append(start)
            
        return res
            
            
            
        
        