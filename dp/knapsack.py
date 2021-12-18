# Solutions for problems from Educative.io


# Solution for 0/1 knapsack using a bottom-up approach 
def solve_knapsack(profits, weights, capacity):
  
  dp = [[0]*(capacity + 1)]*len(profits)

  for i in range(len(profits)):
      dp[i][0] = 0

  for row in range(len(weights)):
      for col in range(1, capacity + 1):
          if row > 0:
              above = dp[row - 1][col]
              if col - weights[row] >= 0:    
                max_with_current = dp[row - 1][col - weights[row]] + profits[row]
                dp[row][col] = max(above, max_with_current)
              else:
                 dp[row][col] = above
          elif row == 0 and col - weights[0] >= 0: #first item
              dp[0][col] = profits[0]

  return dp[len(profits) - 1][capacity]

# Solution for 0/1 knapsack using top down approach with memoization
def solve_knapsack_memoize(profits, weights, capacity):
  dp = [[-1 for c in range(capacity + 1)] for item in range(len(profits))] 
  return knapsack_recursive(profits, weights, capacity, 0, dp)


def knapsack_recursive(profits, weights, capacity, curIndex, dp):
  #handle edge cases
  if capacity <= 0 or curIndex >= len(profits):
    return 0

  # check if solution has already been found
  if dp[curIndex][capacity] != -1:
    return dp[curIndex][capacity]


  #include the current item if fits capacity
  profit1 = 0
  if weights[curIndex] <= capacity:
    profit1 = profits[curIndex] + knapsack_recursive(profits, weights, capacity - weights[curIndex], curIndex + 1, dp)

  # find profit without using current item
  profit2 = knapsack_recursive(profits, weights, capacity, curIndex + 1, dp)
  maxProfit = max(profit1, profit2)
  # store memoized solution
  dp[curIndex][capacity] = maxProfit
  return maxProfit


def main():
  print('Using bottom-up iterative approach')
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print('Using top-down recursive approach with memoization')
  print(solve_knapsack_memoize([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack_memoize([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack_memoize([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()



