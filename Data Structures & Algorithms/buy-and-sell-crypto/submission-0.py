class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()

        profit = 0
        sellPrice = 0

        for price in prices:
            if sellPrice < price:
                sellPrice = price

            newProfit = sellPrice - price

            if newProfit > profit:
                profit = newProfit
            
            print(sellPrice, newProfit)
        
        return profit
