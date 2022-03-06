
#######################################
# Knapsack 0/1
#######################################


# Here is the optimal solution for 0/1 Knapsack
# Time complexity O(c * n), Space complexity O(c)
# We are able to optimize the space complexity by using a single list instead of 2D
# In order to make sure we don't use values that have already been overwritten for the current
# iteration, we have to iterate over the list backwards. The first iteration is handled normally, 
# so for each following iteration the values are always from the previous iteration and can be used to calculate profits
def solve_knapsack(profits, weights, capacity):
  
  dp = [0 for x in range(capacity+1)]

  for i in range(1, capacity+1):
    if weights[0] <= i:
      dp[i] = profits[0]
    
  for i in range(1,len(weights)):
    for j in range(capacity,0,-1):
      profit1 = profit2 = 0
      if j - weights[i] >= 0:
        profit1 = dp[j - weights[i]] + profits[i]
      profit2 = dp[j]
      dp[j] = max(profit1, profit2)

  return dp[-1]   



# Problem Statement - Equal Subset Sum Partition
# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's/2'.
  s = int(s / 2)

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the sum=0 column, as we can always have '0' sum without including 
  # any element
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


# Problem Statement# - Subset Sum
# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

# Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}
#
# Optimal space solution using the same approach as Knapsack 0/1 where we have to iterate in reverse to use values from previous iteration
def can_partition(num, sum):
   
   dp = [False for x in range(sum+1)]
   dp[0] = True
   dp[num[0]] = True

   for i in range(1,len(num)):
      for j in range(sum, 0, -1):
         # include
         include = False
         if num[i] <= j:
            include = dp[j - num[i]]
         # exclude
         exclude = dp[j]

         dp[j] = include or exclude

   return dp[-1]

# Problem Statement - Minimum Subset Sum Difference
# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
#
# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where the minimum absolute difference 
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

def can_partition(num):
  
  total = sum(num)
  dp = [False for x in range(total+1)]
  dp[num[0]] = True
  dp[0] = True
  res = total

  for i in range(1,len(num)):
    for j in range(total, 0, -1):
      include = False
      if j >= num[i]:
        include = dp[j - num[i]]
      exclude = dp[j]
      dp[j] = include or exclude
      if dp[j]:
        sum2 = total - j
        res = min(res, abs(sum2 - j))

  return res


# Problem Statement - Count of subset Sum
# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
#
# Input: {1, 1, 2, 3}, S=4
# Output: 3
# The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
# Note that we have two similar sets {1, 3}, because we have two '1' in our input.
#
#Input: {1, 2, 7, 1, 5}, S=9
# Output: 3
# The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

# Same approach where we can optimize to O(1) space by iterating backwards and using only one row
# Iterating backwards allows us to use values from previous iteration without overwriting numbers we need in the process
def count_subsets(nums, target):
  dp = [0 for col in range(target + 1)] 
  dp[0] = 1

  for i in range(1, len(nums)):
    for j in range(target, 0, -1):
      include = 0
      #exclude
      exclude = dp[j]
      #include
      if j >= nums[i] and dp[j-nums[i]] != 0:
        include = dp[j - nums[i]] + 1

      dp[j] = include + exclude 

  return dp[target]




# Problem Statement - Target Sum
# Given a set of positive numbers (non zero) and a target sum ‘S’.
#  Each number should be assigned either a ‘+’ or ‘-’ sign.
#  We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.
#
# Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
#
# Input: {1, 2, 7, 1}, S=9
# Output: 2
# Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}



