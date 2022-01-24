
## Interval

- [X] [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [X] [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [X] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [ ] [Meeting Rooms (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms/)
- [ ] [Meeting Rooms II (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms-ii/)


The key to most of these interval problems is to first sort them by their start value
```python
#Sort intervals by start value (number in 0 index)
intervals.sort(key = lambda x:x[0])
```

### Merge Intervals ###
Remember to sort these by the start values. We'll keep track of the current interval and the next interval to determine if we need to merge them. If they don't need to be merged we'll add current interval to result list and move on to the next. In order to merge them we just keep the start value and change the end value to whichever is great.
```python
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
```

### Insert Interval ###
The key to inserting interval is knowing that at max we'll merge two intervals with the new interval. All of the other intervals can be placed into intervals to the left and right of the new interval. O(n) time and O(n) space

Remember this pattern ```return left + [[start, end]] + right ``` where left&right are lists of intervals and start&end is the newInterval after we've checked if its two neighbors need to merge or not. Addition operator for Python lists just combines the lists into one.

```python
    def insert_interval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return left + [[start, end]] + right
```

### Non Overlapping Intervals ###
I used a greedy algo approach for this. I sorted intervals by start value, then iterated the list of all intervals.
If there was an overlap, I increment the result count then chose to keep the interval with the smallest end value

```python
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res, interval = 0, intervals[0]
        
        for i in range(1,len(intervals)):
            start, end = interval[0], interval[1]
            nextStart, nextEnd = intervals[i][0], intervals[i][1]    
            if nextStart < end:
                # overlap - determine which interval to keep
                if nextEnd < end:
                    interval = [nextStart, nextEnd]
                res += 1
            else:
                # no overlap
                interval = [nextStart, nextEnd]
        return res
```