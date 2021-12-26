class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        elif n == 1:
            return nums[0]
        # here we just do house robber 1 but either start at the first or second house
        # to deal with the circular neighborhood constraint
        return max(self.rob_dp(nums[1:]), self.rob_dp(nums[:-1])) 

    # this is a good solution for House Robber 1 with O(1) space and O(n) time
    # we only need to keep track of the max values of robbing the prev house or not robbing the prev house
    def rob_dp(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        elif n == 1:
            return nums[0]

        rob, dont_rob = 0,0 #these are max vals of previous house decisions
        for i in range(n):
            robCurrent = max(dont_rob + nums[i], rob)
            dont_rob = rob
            rob = robCurrent
        return max(rob, dont_rob)

   