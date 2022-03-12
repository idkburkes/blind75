

# This is actually similar to a BFS approach. Each pass we'll figure out what is the max reachable in the current range.
# The initial state is the max reachable is whatever the first number is.
# We'll mark that as our last jump position then iterate the array up to that point, finding the max reachable within our range
# Once we reach our last jump position, we'll set the next jump position to whatever we found to be the max reachable 
# This is similar to a BFS 'level'
# We'll continue this process until the jump position is outside of the array, this means we can reach the end  

class Solution:
    def jump(self, nums: List[int]) -> int:
      n = len(nums)
      i = jumps = lastJumpPos = maxReachable = 0
      while lastJumpPos < n - 1:
        maxReachable = max(maxReachable, i + nums[i])
        if i == lastJumpPos:
          lastJumpPos = maxReachable
          jumps += 1
        i += 1
      
      return jumps