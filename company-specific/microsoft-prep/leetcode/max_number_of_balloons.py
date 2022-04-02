class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        target = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        seen =  {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        
        for c in text:
            if c in seen:
                seen[c] = seen[c] + 1
        res = float('inf')  
        
        for char, freq in seen.items():
            res = min(res, seen[char] // target[char])
        
        return res
        