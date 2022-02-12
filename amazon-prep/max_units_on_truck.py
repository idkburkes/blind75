

from heapq import heappush, heappop

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxheap, res, load = [], 0, 0
        for box in boxTypes:
            heappush(maxheap, (-box[1], box[0]))
            
        while maxheap and load <= truckSize:
            box = heappop(maxheap)
            units, numBoxes = -box[0], box[1]
            while numBoxes > 0 and load + 1 <= truckSize:
                res += units
                load += 1
                numBoxes -= 1
        return res
            
            
            
        