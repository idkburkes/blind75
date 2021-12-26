class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices or n <= 1:
            return 0
        start, max, end = 0, 0, 1
        while end < n:
            if prices[end] < prices[start]:
                start = end
            elif prices[end] - prices[start] > max:
                max = prices[end] - prices[start]
            end += 1
        return max


