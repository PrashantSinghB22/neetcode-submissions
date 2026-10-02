class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min = prices[0]

        for price in prices:
            profit = price - min
            max_profit = max(max_profit, profit)

            if price < min:
                min = price
        return max_profit
            
