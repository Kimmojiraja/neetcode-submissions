class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0 
        minprice = prices[0] # it will start from the first index 

        for sell in prices:
            maxprofit = max(maxprofit, sell-minprice) # clear profit
            minprice = min(minprice,sell) # now taking the loop to find the minprice
        return maxprofit



        