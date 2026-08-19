class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        small = prices[0]
        for i in range(len(prices)):
            if prices[i] < small:
                small = prices[i]
            if prices[i] - small > profit :
                profit = prices[i] - small

        return profit 
            


       
        