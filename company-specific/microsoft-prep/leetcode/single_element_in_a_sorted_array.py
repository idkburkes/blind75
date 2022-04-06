class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            halves_are_even = (right - mid) % 2 == 0 
            
            if nums[mid] == nums[mid - 1]: #matching on the left  
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            elif nums[mid] == nums[mid + 1]:  #matching on the right
                if halves_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]
            
        return nums[left]
              
    
        # [1,1,2,2,3,3,5,5,9]