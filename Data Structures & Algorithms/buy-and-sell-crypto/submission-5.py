class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min = prices[0]

        # for price in prices:
        #     profit = price - min
        #     max_profit = max(max_profit, profit)

        #     if price < min:
        #         min = price
        # return max_profit

        max_profit = 0
        l = 0
        r = 1

        while r < len(prices): 
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

        return max_profit


            
