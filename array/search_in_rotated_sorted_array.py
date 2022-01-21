class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        #find smallest val in array using binary search in log(n) time
        left, right = 0, n-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # the rotation is equal to the index of the smallest value in array        
        rot = left
                
        # perform binary search accounting for the rotation in log(n) time
        left, right = 0, n-1
        while left <= right:
            mid = left + (right - left ) // 2
            realMid = (mid + rot) % n
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
                
        