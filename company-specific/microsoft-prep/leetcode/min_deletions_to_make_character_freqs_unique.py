from heapq import heappop, heappush

class Solution:
    def minDeletions(self, s: str) -> int:
        
        freqs = dict()
        
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1
        
        maxheap = []
        for char, freq in freqs.items():
            heappush(maxheap, (-freq, char))
            
        deletions = 0
        while maxheap:
            freq, char = heappop(maxheap)
            if maxheap and freq == maxheap[0][0]:
                deletions += 1
                freq += 1
                if freq != 0:
                    heappush(maxheap, (freq, char))
                
        return deletions
            
        