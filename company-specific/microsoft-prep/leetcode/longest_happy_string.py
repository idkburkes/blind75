from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        if a != 0:
            heappush(heap, (-a, 'a') )
        if b != 0:
            heappush(heap, (-b, 'b') )
        if c != 0:
            heappush(heap, (-c, 'c') )
        res = ''
        
        while heap:
            freq, char = heappop(heap)
            
            if len(res) > 1 and res[-1] == res[-2] == char:
                # if there is no alternative then we're done
                if not heap:
                    return res
                
                # take the next char if this has been repeated twice
                skippedChar = (freq, char)
                freq, char = heappop(heap)
                heappush(heap, skippedChar)
            
            # add this char to result
            res += char
            # since we're using negative nums we increment frequency
            freq += 1
            
            if freq != 0:
                heappush(heap, (freq, char))
        
        return res
            
                    
        
        
        
        
        
        