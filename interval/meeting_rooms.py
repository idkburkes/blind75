class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x:x[0])
        interval = intervals[0]
        for i in range(1,len(intervals)):
            next_int = intervals[i]
            if next_int[0] < interval[1]:
                return False
            interval = next_int
        return True
        