
# This is Floyd's Cycle Detection Algorithm

# It is key to remember that the distance from the starting point to the beginning of the cycle 
# is the same length as from the intersection point to the beginning of the cycle

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        first = True
        
        # Find the intersection point
        while slow != fast or first:
            first = False
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Move slow pointer back to the start
        slow = nums[0]
        
        # Traverse until slow&fast intersect at the beginning of the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
             
        return fast
        