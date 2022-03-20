#######################################
# Longest Common Substring
#######################################
#
# Problem Statement - Longest Common Substring
# Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.
#--------------------
# Example 1:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 2
# Explanation: The longest common substring is "bd".
#-------------------
# Example 2:
# Input: s1 = "passport"
#       s2 = "ppsspt"
# Output: 3
# Explanation: The longest common substring is "ssp".

def find_LCS_length(s1, s2):
  m = len(s1)
  n = len(s2)
  res = 1
  dp = [[0 for col in range(n)] for row in range(m)]

  # populate first col
  for i in range(m):
    if s1[i] == s2[0]:
      dp[i][0] = 1
      res = 1
  # populate first row
  for i in range(n):
    if s1[0] == s2[i]:
      dp[0][i] = 1
      res = 1
# An alternative to prepopulating the first row & column is to add
# an extra row and column full of zeros, this way we could start on row 1 column 1 without
# ArrayOutOfBounds exceptionds
#
# After gaining more experience I have found that I prefer to use the extra row & column. See next question

  for i in range(1,m):
    for j in range(1,n):
      # If two letters are the same then the current length of common substring is 1 + the
      # length from the previous letter in both words   
      if s1[i] == s2[j]:
        dp[i][j] = dp[i-1][j-1] + 1
        res = max(res, dp[i][j])
  return res

 

# Problem Statement - Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
# without changing the order of the remaining elements.
#
# Example 1:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 3
# Explanation: The longest common subsequence is "bda".
#
# Example 2:
# Input: s1 = "passport"
#      s2 = "ppsspt"
# Output: 5
# Explanation: The longest common subsequence is "psspt".
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
    m = len(text1)
    n = len(text2)
    dp = [[0 for col in range(n+1)] for row in range(m+1)]
    res = 0
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            res = max(res, dp[i][j])
        
    return res


# Problem Statement - Minimum Deletions & Insertions to Transform a String into another
# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.

# Example 1:
# Input: s1 = "abc"
#      s2 = "fbc"
# Output: 1 deletion and 1 insertion.
# Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

# Example 2:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 2 deletions and 1 insertion.
# Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

# Example 3:
# Input: s1 = "passport"
#       s2 = "ppsspt"
# Output: 3 deletions and 1 insertion
# Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

# THE SOLUTION PATTERN FOR MINIMUM DELETIONS & INSERTIONS
# Seeing this type of question, it is a huge indicator that we'll need to use the longest subsequence or subsequence then
# subtract it from some known value (like the length of the string). This has shown up multiple times and it has stumped
# me now and a few times in the past. Learn this!!!

# Solution
# This problem can easily be converted to the Longest Common Subsequence (LCS).
# If we can find the LCS of the two input strings, we can easily find how many characters we need to insert and delete from s1.
# Here is how we can do this:

# 1. Let’s assume len1 is the length of s1 and len2 is the length of s2.
# 2. Now let’s assume c1 is the length of LCS of the two strings s1 and s2.
# 3. To transform s1 into s2, we need to delete everything from s1 which is not part of LCS, 
#           so minimum deletions we need to perform from s1 => len1 - c1
# 4. Similarly, we need to insert everything in s1 which is present in s2 but not part of LCS,
#           so minimum insertions we need to perform in s1 => len2 - c1
def find_MDI(s1, s2):
  c1 = find_LCS_length(s1, s2)
  print("Minimum deletions needed: " + str(len(s1) - c1))
  print("Minimum insertions needed: " + str(len(s2) - c1))


def find_LCS_length(s1,  s2):
  n1, n2 = len(s1), len(s2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  maxLength = 0
  for i in range(1, n1+1):
    for j in range(1, n2+1):
      if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + dp[i - 1][j - 1]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

      maxLength = max(maxLength, dp[i][j])

  return maxLength

# Problem Statement - Longest Increasing Subsequence
# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
# In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
#
# Example 1:
# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LIS is {2,3,6,10,12}.
#
# Example 2:
# Input: {-4,10,3,7,15}
# Output: 4
# Explanation: The LIS is {-4,3,7,15}.
#
# This is a classic DP question that I should know how to do off the dome.
# Its a 1D dp problem with O(n^2) time

# 1. If the number at the current index is bigger than the number at the previous index, 
#              we increment the count for LIS up to the current index.
# 2. But if there is a bigger LIS without including the number at the current index, we take that.
#
# So we need to find all the increasing subsequences for the number at index ‘i’, 
# from all the previous numbers (i.e. number till index ‘i-1’), to eventually find the longest increasing subsequence.

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    res = 1
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                res = max(res, dp[i])
    return res

# Problem Statement - Maximum Sum Increasing Subsequence
# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.
#
# Example 1:
# Input: {4,1,2,6,10,1,12}
# Output: 32
# Explanation: The increaseing sequence is {4,6,10,12}. 
# Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
#
# Example 2:
# Input: {-4,10,3,7,15}
# Output: 25
# Explanation: The increaseing sequences are {10, 15} and {3,7,15}.

# Pretty similar to maximum increasing subsequence, but instead of checking if the current dp length + 1 is greater than
# the longest length, we check if the current dp sum + the ith number is greater than the sum at dp[i] 
def find_MSIS(nums):
      n = len(nums)
      dp = [0] * n
      dp[0] = nums[0]
      res = nums[0]

      for i in range(1,n):
        dp[i] = nums[i]
        for j in range(i):
          if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
            dp[i] = dp[j] + nums[i]
          res = max(res, dp[i])

      return res


# Problem Statement - Shortest Common Supersequence 
# Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

# Example 1:
# Input: s1: "abcf" s2:"bdcf" 
# Output: 5
# Explanation: The shortest common super-sequence (SCS) is "abdcf". 
#
# Example 2:
# Input: s1: "dynamic" s2:"programming" 
# Output: 15
# Explanation: The SCS is "dynprogrammicng". 

# The solution here is to realize that the length of the longest common subsequence + count of chars from string1 not contained
# in LCS + count of chars from string2 not contained in LCS is the length of the shortest common subsequence
def find_SCS_length(s1, s2):
  
  m = len(s1)
  n = len(s2)
  dp = [[0 for col in range(n+1)] for row in range(m+1)]

  # Find the longest common subsequence
  # we've already done this in a previous problem
  for i in range(1,m+1):
    for j in range(1,n+1):
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      if s1[i-1] == s2[j-1]:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

  # longest common subsequence
  lcs = dp[m][n]
  # chars in string1 that weren't in LCS
  remaining1 = m - lcs
  # chars in string2 that weren't in LCS
  remaining2 = n - lcs

  # sum all of these to get the shortest common super-sequence
  return lcs + remaining1 + remaining2

# Problem Statement - Minimum Deletions to make a sequence sorted 
# Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

# Example 1:
# Input: {4,2,3,6,10,1,12}
# Output: 2
# Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.

# Example 2:
# Input: {-4,10,3,7,15}
# Output: 1
# Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.

# Example 3:
# Input: {3,2,1,0}
# Output: 3
# Explanation: Since the elements are in reverse order, we have to delete all except one to get a 
# sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}

# I had problems recalling the longest increasing subsequence pattern from memory. Practice this a few times.
def find_minimum_deletions(nums):
  n = len(nums)
  dp = [1] * n
  dp[0] = 1
  # Longest increasing subsequence
  LIS = 1
  for i in range(1,n):
    for j in range(i):
      if nums[i] > nums[j] and dp[i] <= dp[j]:
        dp[i] = dp[j] + 1
        LIS = max(LIS, dp[i])

  # Minimum deletions is difference between length of array and LIS
  min_dels = n - LIS
  return min_dels


# Problem Statement - Longest Repeating Subsequence
# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# Example 1:
# Input: “t o m o r r o w”
# Output: 2
# Explanation: The longest repeating subsequence is “or” {tomorrow}.
#
# Example 2:
# Input: “a a b d b c e c”
# Output: 3
# Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.
#
# Example 3:
# Input: “f m f f”
# Output: 2
# Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.
#
# The problem is quite similar to the Longest Common Subsequence (LCS), with two differences:
# In LCS, we were trying to find the longest common subsequence between the two strings, whereas in LRS we are trying to find the two longest common subsequences within one string.
# In LRS, every corresponding character in the subsequences should not have the same index.
#
# If the two indexes are not the same and the characters at both the indexes are same, we can recursively match for the remaining length (i.e. by incrementing both the indexes).
# If the characters at both the indexes don’t match, we start two new recursive calls by incrementing each index separately. The LRS would be the one with the highest length from the two recursive calls.
#
# I think for this problem it would be helpful to take a look at the top-down approach with memoization for some intuition
def find_LRS_length(str):
  n = len(str)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  return find_LRS_length_recursive(dp, str, 0, 0)


def find_LRS_length_recursive(dp,  str, i1, i2):
  n = len(str)
  if i1 == n or i2 == n:
    return 0

  if dp[i1][i2] == -1:
    if i1 != i2 and str[i1] == str[i2]:
      dp[i1][i2] = 1 + find_LRS_length_recursive(dp, str, i1 + 1, i2 + 1)
    else:
      c1 = find_LRS_length_recursive(dp, str, i1, i2 + 1)
      c2 = find_LRS_length_recursive(dp, str, i1 + 1, i2)
      dp[i1][i2] = max(c1, c2)

  return dp[i1][i2]

# Here is the bottom-up solution with O(n^2) time complexity
def find_LRS_length(s):
  n = len(s)
  # the longest repeating subsequence we compare chars in a string to other chars in the same string so its an NxN matrix
  dp = [[0 for col in range(n+1)] for row in range(n+1)]
  LRS = 0
  for i in range(1,n+1):
    for j in range(1,n+1):
      if s[i-1] == s[j-1] and i != j:
        # If its a match with different indices then the length is incremented by 1 + the max from the previous letter in "both" strings
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        # If its not a valid match, then we take the max from either 1 char back in the column's string or 1 char back in the row's string
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      LRS = max(LRS, dp[i][j])

  return LRS



# Problem Statement - Subsequence Pattern Matching
# Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.
#
# Example 1: Input: string: “baxmx”, pattern: “ax”
# Output: 2
# Explanation: {baxmx, baxmx}.
#
# Example 2:
# Input: string: “tomorrow”, pattern: “tor”
# Output: 4
# Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.
#
# Since we want to match all the subsequences of the given string, we can use a two-dimensional array to store our results. 
# As mentioned above, we will be tracking separate indexes for the string and the pattern, so we will be doing two things for every value of strIndex and patIndex:
# 1. If the character at the strIndex (in the string) matches the character at patIndex (in the pattern),
#    the count of the SPM would be equal to the count of SPM up to strIndex-1 and patIndex-1.
# 2. At every step, we can always skip a character from the string to try matching the remaining string with the pattern;
#    therefore, we can add the SPM count from the indexes strIndex-1 and patIndex.

def find_SPM_count(str, pat):
  m = len(str)
  n = len(pat)
  # init extra row and column for empty subsequence and empty string in beginning
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

  # all subsequences with empty pattern is a match
  for i in range(m+1):
    dp[i][0] = 1

  for i in range(1, m+1):
    for j in range(1, n+1):
      # If chars match then the number of matches is the same as number of matches from previous chars in both
      if str[i-1] == pat[j-1]:
        dp[i][j] = dp[i-1][j-1]
      # At every step we add the amount of matches for this char in the pattern
      dp[i][j] += dp[i-1][j]

  return dp[m][n]


# Problem Statement - Longest Bitonic Subsequence
# Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS).
# A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

# Example 1:
# Input: {4,2,3,6,10,1,12}
# Output: 5
# Explanation: The LBS is {2,3,6,10,1}.

# Example 2:
# Input: {4,2,5,9,7,6,10,3,1}
# Output: 7
# Explanation: The LBS is {4,5,9,7,6,3,1}.

# The solution is to find the longest increasing subsequence from each point then find the longest decreasing subsequence from each point.
# The max sum of these from each point will give us the solution. Remember to substract 1 from the max sum so we don't include the current number twice
# Also will have to remember that finding the longest decreasing subsequence is slightly different from LIS. 
# We'll have to do the process in reverse, so we start from the last index and iterate towards the beginning of the array
def find_LBS_length(nums):
  n = len(nums)
  # Longest increasing subsequence
  lis = [1 for _ in range(n)]
  # Longest decreasing subsequence
  lds = [1 for _ in range(n)]

  # find longest increasing subsequence from every point the beginning, start from the beginning
  for i in range(n):
    for j in range(i):
      if nums[j] < nums[i]:
        lis[i] = max(lis[i], lis[j] + 1)

  # find longest decreasing subsequence from evrey point to the end, starting from the end
  for i in range(n-1, -1, -1):
    for j in range(i+1, n):
      if nums[j] < nums[i]:
        lds[i] = max(lds[i], lds[j] + 1)
    
  # find sum of LIS and LDS from each point
  # the longest bitonic subsequence is the max sum
  LBS = 1
  for i in range(n):
    # subtract 1 so you don't include the current number twice
    LBS = max(lis[i] + lds[i] - 1, LBS)

  return LBS


# Problem Statement - Longest Alternating Subsequence
# Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
# A subsequence is considered alternating if its elements are in alternating order.
#
# A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:
# {a1 > a2 < a3 } or { a1 < a2 > a3}. 
# Example 1:
# Input: {1,2,3,4}
# Output: 2
# Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
#
# Example 2:
# Input: {3,2,1,4}
# Output: 3
# Explanation: The LAS are {3,2,4} and {2,1,4}.
#
# Example 3:
# Input: {1,3,2,4}
# Output: 4
# Explanation: The LAS is {1,3,2,4}.
#
#
# Detailed solution explanation
# 1. We need to find an ascending and descending subsequence at every index.
# 2. While finding the next element in the ascending order, if the number at the current index is bigger than the number at the previous index,
#    we increment the count for a LAS up to the current index. But if there is a bigger LAS without including the number at the current index, we take that.
# 3. Similarly for the descending order, if the number at the current index is smaller than the number at the previous index,
#    we increment the count for a LAS up to the current index. But if there is a bigger LAS without including the number at the current index, we take that.

# To find the largest LAS, we need to find all of the LAS for a number at index ‘i’ from all the previous numbers (i.e. number till index ‘i-1’).
# We can use two arrays to store the length of LAS, one for ascending order and one for descending order. 
# (Actually, we will use a two-dimensional array, where the second dimension will be of size two).

# If ‘i’ represents the currentIndex and ‘j’ represents the previousIndex, our recursive formula would look like:

# If nums[i] is bigger than nums[j] then we will consider the LAS ending at ‘j’ where the last two elements were in descending order =>
#      if num[i] > num[j] => dp[i][0] = 1 + dp[j][1], if there is no bigger LAS for 'i'
# If nums[i] is smaller than nums[j] then we will consider the LAS ending at ‘j’ where the last two elements were in ascending order =>
#      if num[i] < num[j] => dp[i][1] = 1 + dp[j][0], if there is no bigger LAS for 'i'

def find_LAS_length(nums):
  
  n = len(nums)
  dp = [[1 for _ in range(n)] for _ in range(2)]

  # [0][] first row is ascending index
  # [1][] second row is descending index
  for i in range(1,n):
    for j in range(i): # this loop gives us O(n^2) time complexity
      if nums[i] > nums[j]:
        # if nums are ascending then increment from max length where numbers were last descending
        dp[0][i] = max(dp[0][i], dp[1][j] + 1)
      else:
        # if nums are descending then increment from max length where numbers were last ascending
        dp[1][i] = max(dp[1][i], dp[0][j] + 1)

  # return the max length from either ascending or descending array
  return max(dp[0][n-1], dp[1][n-1])

# Problem Statement - Edit Distance
# Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters.
# Write a function to calculate the count of the minimum number of edit operations.

# Example 1:
# Input: s1 = "bat"
#      s2 = "but"
# Output: 1
# Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
#
# Example 2:
# Input: s1 = "abdca"
#      s2 = "cbda"
# Output: 2
# Explanation: We can replace first 'a' with 'c' and delete second 'c'.
#
# Example 3:
# Input: s1 = "passpot"
#      s2 = "ppsspqrt"
# Output: 3 
# Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

# The key here is knowing that if the current letters match then we take the prev length from before each letter in both words
# if the letters don't match, then we have to increment by the minimum between excluding the first word, excluding the second word,
# or excluding both words, which technically counts as an "edit" operation.
#
# There are a couple edge cases we have to handle by init the first rows and columns with their index
# this is for the base case that either word is empty
#
# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gx2QMvEorYY
def editDistance(self, word1: str, word2: str) -> int:
  m = len(word1)
  n = len(word2)
  
  # if either string is empty, return the length of the other
  if n * m == 0:
      return n + m
  
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
  
  # if word2 is empty we can remove all letters in word1
  for i in range(m+1):
      dp[i][0] = i
  
  # if word1 is empty we can add all letters in word2
  for i in range(n+1):
      dp[0][i] = i
  
  for i in range(1,m+1):
      for j in range(1,n+1):
          if word1[i-1] == word2[j-1]:
              dp[i][j] = dp[i-1][j-1]
          else:
              dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  
  return dp[m][n]

  # Problem Statement - Strings Interweaving
# Given three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’
# would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

# Example 1:
# Input: m="abd", n="cef", p="abcdef"
# Output: true
# Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too. 
#
# Example 2:
# Input: m="abd", n="cef", p="adcbef"
# Output: false
# Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order. 
#
# Example 3:
# Input: m="abc", n="def", p="abdccf"
# Output: false
# Explanation: 'p' does not contain all the letters from 'm' and 'n'. 
#
# Example 4:
# Input: m="abcdef", n="mnop", p="mnaobcdepf"
# Output: true
# Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too. 

def find_SI(string1, string2,  interweaved):

  m = len(interweaved)
  n1 = len(string1)
  n2 = len(string2)

  dp1 = [[0 for _ in range(n1+1)] for _ in range(m+1)]
  dp2 = [[0 for _ in range(n2+1)] for _ in range(m+1)]

  for i in range(1,m+1):
    # LCS for string1
    for j in range(1,n1+1):
      if interweaved[i-1] == string1[j-1]:
        dp1[i][j] = 1 + dp1[i-1][j-1]
      else:
        dp1[i][j] = max(dp1[i][j-1], dp1[i-1][j])
    # LCS for string2
    for k in range(n2+1):
      if interweaved[i-1] == string2[k-1]:
        dp2[i][k] = 1 + dp2[i-1][k-1]
      else:
        dp2[i][k] = max(dp2[i-1][k], dp2[i][k-1])
  
  # Check if longest common subsequence for both strings is the entire string itself
  return dp1[m][n1] == n1 and dp2[m][n2] == n2 and m == n1 + n2 