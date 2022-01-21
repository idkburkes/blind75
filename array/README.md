
## Array

- [X] [Two Sum](https://leetcode.com/problems/two-sum/)
- [X] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [X] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [ ] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [X] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [X] [3Sum](https://leetcode.com/problems/3sum/)
- [X] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)


Common Patterns in Array problems
- Hashmaps and sets for O(1) retrieval
- Kadane's Algorithm
- Sliding Window/Two pointers
## Kadane's Algorithm (Maximum subarray)
[![Kadane's Algorithm](./kadanes_algorithm.png)](https://www.youtube.com/watch?v=jnoVtCKECmQ)


### Container with most water ###
Pretty easy two pointer problem.

```Python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
      
        maxarea, left, right = 0, 0, n-1
        while left < right:
            minh = min(height[left], height[right])
            dist = right - left 
            maxarea = max(maxarea, minh * dist)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea     

```
