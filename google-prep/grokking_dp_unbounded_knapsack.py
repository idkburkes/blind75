
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

  