class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for ind in range(len(prices)):
            if prices[ind] < prices[buy]:
                buy = ind
            else:
                max_profit = max(max_profit, prices[ind] - prices[buy])
        return max_profit