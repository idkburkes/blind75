
## Interval

- [ ] [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [X] [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [ ] [Meeting Rooms (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms/)
- [ ] [Meeting Rooms II (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms-ii/)


The key to most of these interval problems is to first sort them by their start value
```python
#Sort intervals by start value (number in 0 index)
intervals.sort(key = lambda x:x[0])
```