from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        
        heap = []
        
        for interval in intervals:
            # Check if current interval's start time is after the latest ongoing meeting's time
            # If it is then we don't need to allocate a new room, so we just replace the interval 
            if heap and interval[0] >= heap[0]:
                heappop(heap)
                heappush(heap, interval[1])
            # If this is the first meeting or if the current meeting's start time is before the latest
            # ongoing meeting's end time then we need to allocate a new room by adding this interval to the heap
            else:
                heappush(heap, interval[1])
                
        # the size of the heap will represent max amount of rooms we needed at any one time
        return len(heap)