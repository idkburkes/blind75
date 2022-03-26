def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n <= 1:
        return intervals
    
    intervals.sort(key = lambda x:x[0])
    interval = intervals[0]
    res = []
    
    for i in range(1, n):
        nextinterval = intervals[i]
        if nextinterval[0] <= interval[1]:
            interval[0] = min(nextinterval[0], interval[0])
            interval[1] = max(nextinterval[1], interval[1])
        else:
            res.append(interval)
            interval = nextinterval
            
    #don't forget to add the last interval
    res.append(interval)
    
    return res