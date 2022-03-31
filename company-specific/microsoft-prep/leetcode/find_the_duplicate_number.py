class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]
        first = True
        
        while first or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            first = False
            
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        