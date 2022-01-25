class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n & 1 == 1: # if the first bit is set
                res += 1
            n = n >> 1 # shift bits to the right
        return res