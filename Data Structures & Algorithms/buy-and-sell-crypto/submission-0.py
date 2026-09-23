class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high
        # buy on one of the days and sell on a different day
        # left point on day 1 right pointer on day 2
        # left = buy, right = sell
        # track maxProfit -> when right val > left val

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # want left pointer to be at the minimum
            r += 1
        return maxP