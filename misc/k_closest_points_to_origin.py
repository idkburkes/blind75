from math import sqrt
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        res, heap = [], []
        
        # Push the first k onto max-heap
        for i in range(k):
            x, y = points[i][0], points[i][1]
            dist = sqrt((x ** 2) + (y ** 2)) 
            heappush(heap, (-dist, x, y))
        
        # If we find point closer to origin then pop max distance and push new point onto heap
        for i in range(k, len(points)):
            x, y = points[i][0], points[i][1]
            dist = sqrt((x ** 2) + (y ** 2))
            if dist < -heap[0][0]:
                heappop(heap)
                heappush(heap, (-dist, x, y))
        
        while len(heap):
            dist, x, y = heappop(heap)
            res.append([x,y])
        return res
            
                
            
        
        
        
    

        
        
        