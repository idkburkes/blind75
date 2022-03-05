from heapq import heappush, heappop

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        freqs = {}
        heap = []
        
        for num in arr:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num, freq in freqs.items():
            heappush(heap, (freq, num))
        
        while heap:
            freq, _ = heappop(heap)
            k -= freq
            if k == 0:
                return len(heap)
            elif k < 0:
                return len(heap) + 1