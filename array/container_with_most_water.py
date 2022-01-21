class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
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
            
        