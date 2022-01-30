
# Binary

- [X] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [X] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [X] [Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

---

### Sum of Two Integers ###

There is a whole lot going on here so get ready!

In order to sum two integers we need the xor + the carry bits.
We calculate the carry bits by a & b -> then shifting the anded bits once to the left with ```(a&b) << 1```
We calculate the xor bits by using ```a^b```
We continue doing this in a loop. The logic here is that once the carry equals 0, then the XOR at that point will be the actual sum 

Handling negative numbers
Python is not going to automatically handle negative numbers.
Instead of seeing a number that looks like 0xFFFFFFEC it interprets it as an arbitrarily large integer 0x0000000000000FFFFFFEC. Since there are all zeros to the left it is a LARGE integer number instead of a signed 32 bit integer. We can convert this to a signed 32 bit integer by taking the twos complement.

Trick for taking two's complement in Python
```~(num^mask)```

A more detailed discussion of the derivation of this can be found [here](https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python)



```python
    def getSum(self, a: int, b: int) -> int:
         # This mask is set so that integers stay at 32 bits
         # Apparently Python handles integer lengths beyond 32 bits
         # If we and them with this mask all bits beyond 32 will be zeroed out
        mask = 0xFFFFFFFF

        while b != 0:
            xor = (a^b) & mask
            carry = ((a&b) << 1) & mask
            a = xor
            b = carry
            
        if (a>>31) == 1:
            return ~(a^mask)
        else:
            return a
```

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