from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        maxheap = []
        res = []
        freqs = dict()
        
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
        
        for word, freq in freqs.items():
            heappush(maxheap, (-freq, word))
        
        for _ in range(k):
            if maxheap:
                freq, word = heappop(maxheap)
                res.append(word)
            
        return res
            
        