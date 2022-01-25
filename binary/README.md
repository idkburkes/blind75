
# Binary

- [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [X] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [X] [Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

---



### Number of 1 bits ###
To count the number of bits in a number we'll check if the first bit is set then shift the bits right until the number equals 0. This has a time complexity of O(logn) because each time we shift the bits right it is essentially dividing the number by 2
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n & 1 == 1: # if the first bit is set
                res += 1
            n = n >> 1 # shift bits to the right
        return res
```

### Counting Bits ###
```python
# This is the naive solution with O(nlogn) time complexity
def countBits(self, n: int) -> List[int]:
    res = []
    for num in range(0,n+1):
        bits = 0
        # This while loop takes logn time
        while num > 0:
            if num & 1 == 1:
                bits += 1
            num = num >> 1
        res.append(bits)
    return res

# This is the optimal solution with O(n) time complexity
# (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
def countBitsOptimal(self, n: int) -> List[int]:
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i & (i-1)] + 1
    return dp
```