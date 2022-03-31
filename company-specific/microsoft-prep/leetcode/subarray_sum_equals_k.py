class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum = res = 0
        sum_map = {0:1} # base case if cursum == k

        for i in range(len(nums)):
            cursum += nums[i]
            
            # find how many previous subarray prefixes, 
            #   if removed, would make the current subarray == k
            if cursum - k in sum_map:
                res += sum_map[cursum - k]
                
            # add or increment current subarray prefix sum to map
            sum_map[cursum] = sum_map.get(cursum, 0) + 1
        
        return res
            
        