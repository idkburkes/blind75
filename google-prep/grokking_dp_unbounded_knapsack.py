
#######################################
# Unbounded Knapsack
#######################################

# Problem Statement - Unbounded Knapsack
# Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’.
# We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.

# The difference in the unbounded knapsack approach from 0/1 is that we have to include the option to include the first
# number multiple times in the first row, so we don't skip over filling the first row
def solve_knapsack(profits, weights, capacity):
  N = len(weights)
  dp = [[0 for col in range(capacity + 1)] for row in range(N)]

  for i in range(N):
    for j in range(capacity + 1):
      include = exclude = 0
      if i > 0:
        exclude = dp[i-1][j]
      if j >= weights[i]:
        include = profits[i] + dp[i][j - weights[i]]
      dp[i][j] = max(include, exclude)

  return dp[N-1][capacity]


# Problem Statement - Rod Cutting
# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the profit. 
# We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.
#
# Another big change is you CANT OPTIMIZE FOR O(capacity) space in unbounded knapsack because you need the
# previous values from the current row to get the max value on each iteration

def solve_rod_cutting(lengths, prices, total_length):
  n = len(prices)
  dp = [[0 for col in range(total_length+1)] for row in range(n)]

  for i in range(n):
    for j in range(total_length+1):
      include = exclude = 0
      if i > 0:
        exclude = dp[i-1][j]
      if j >= lengths[i]:
        include = prices[i] + dp[i][j - lengths[i]]
      dp[i][j] = max(include, exclude)

  return dp[n-1][total_length]

# Problem Statement - Coin Count
# Given a number array to represent different coin denominations and a total amount ‘T’,
# we need to find all the different ways to make a change for ‘T’ with the given coin denominations.
# We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.
#
# Same exact approach as last problem

def count_change(denominations, total):
  n = len(denominations)
  dp = [[0 for col in range(total+1)] for row in range(n)]

  for i in range(n):
    dp[i][0] = 1

  for i in range(n):
    for j in range(total + 1):
      include = exclude = 0
      if i > 0 and dp[i-1][j]:
        exclude = dp[i-1][j]
      if j >= denominations[i]:
        include = dp[i][j - denominations[i]] + 1

      dp[i][j] = max(include, exclude)

  return dp[n-1][total]


# Problem Statement - Minimum Coin Change
# Given a number array to represent different coin denominations and a total amount ‘T’,
# we need to find the minimum number of coins needed to make a change for ‘T’.
# We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.

# Example 1:
# Denominations: {1,2,3}
# Total amount: 5
# Output: 2
# Explanation: We need a minimum of two coins {2,3} to make a total of '5'

# Example 2:
# Denominations: {1,2,3}
# Total amount: 11
# Output: 4
# Explanation: We need a minimum of four coins {2,3,3,3} to make a total of '11'


# This problem has a similar approach to the last problem, except instead of optimizing for max value
# we are checking for the minimum value. We can initialize the dp array with infinity so we can use math.min to make comparisons
# Something I messed up on my first run-through of this problem was remembering to use the current row for calculating the include
# value. This is characteristic of all Unbounded Knapsack problems and this is how its different than Knapsack 0/1.
def count_change(denominations, total):
  n = len(denominations)
  dp = [[float('inf') for col in range(total + 1)] for row in range(n)]

  # initialize first column to 0
  for i in range(n):
    dp[i][0] = 0
    
  for i in range(n):
    for j in range(1,total+1):
      include = exclude = float('inf')
      if i > 0:
        exclude = dp[i-1][j]  
      if j >= denominations[i] and dp[i][j - denominations[i]] != float('inf'):
        include = dp[i][j - denominations[i]] + 1
      
      dp[i][j] = min(include, exclude)
      
  return dp[n-1][total] if dp[n-1][total] != float('inf') else -1

# Problem Statement - Maximum Ribbon Cut
# Given a number array to represent possible ribbon lengths and a total ribbon length ‘n,’
# we need to find the maximum number of pieces that the ribbon can be cut into.

# Example 1:
# n: 5
# Ribbon Lengths: {2,3,5}
# Output: 2
# Explanation: Ribbon pieces will be {2,3}.

# Example 2:
# n: 7
# Ribbon Lengths: {2,3}
# Output: 3
# Explanation: Ribbon pieces will be {2,2,3}.

# Example 3:
# n: 13
# Ribbon Lengths: {3,5,7}
# Output: 3
# Explanation: Ribbon pieces will be {3,3,7}.
  

def count_ribbon_pieces(ribbonLengths, total):
  
  n = len(ribbonLengths)
  dp = [[-1 for col in range(total+1)] for row in range(n)]

  # populate the total=0 columns, as we don't need any ribbon to make zero total
  for i in range(n):
    dp[i][0] = 0

  for i in range(n):
    for j in range(1,total + 1):
      include = exclude = -1

      # exclude the ribbon
      if i > 0:
        exclude = dp[i-1][j]

       # include the ribbon and check if the remaining length can be cut into available lengths
      if j >= ribbonLengths[i] and dp[i][j - ribbonLengths[i]] != -1:
        include = dp[i][j - ribbonLengths[i]] + 1

      dp[i][j] = max(include, exclude)
  
  return dp[n-1][total]