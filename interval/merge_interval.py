class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key = lambda x:x[0])
        res = []
        interval = intervals[0]
        
        for i in range(1,len(intervals)):
            start, end = interval[0], interval[1]
            next_start, next_end = intervals[i][0], intervals[i][1]
            if next_start <= end:
                end = max(end, next_end)
                interval = [start, end]
            else:
                res.append(interval)
                interval = [next_start, next_end]
        res.append(interval)
        return res
            
            
            
            
            
            
        