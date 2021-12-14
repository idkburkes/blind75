from heapq import *

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

class MedianFinder:

  def __init__(self):
      self.small_heap = []
      self.big_heap = []
        
  def addNum(self, num: int) -> None:

    # when lengths are equal we'll add to the big heap
    #  -> adding to the big heap means we'll push to the small heap 
    #  -> then pop the biggest value from the small heap and push it to the big heap
    #    
    # when lengths are different we'll add to the small heap
    #  -> adding to the small heap means push to the big heap then pop the smallest
    #     from big heap and put it in the small heap
    if len(self.small_heap) == len(self.big_heap):
      heappush(self.small_heap, -num) # num inverted beccause small heap is max heap
      max_from_small = heappop(self.small_heap)
      heappush(self.big_heap, -max_from_small) #invert to add to min heap
    else:
      heappush(self.big_heap, num)
      min_from_big = heappop(self.big_heap)
      heappush(self.small_heap, -min_from_big)
    
  def findMedian(self) -> float:
      if len(self.small_heap) == len(self.big_heap):
          return (self.big_heap[0] - self.small_heap) / 2.0
      else:
          return self.big_heap[0]
