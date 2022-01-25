


# This is the optimal solution with O(n) time complexity
def countBitsOptimal(self, n: int) -> List[int]:
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i & (i-1)] + 1
    return dp


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