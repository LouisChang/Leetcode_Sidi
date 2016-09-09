class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #check edge case
        if prices  == []:
            return 0
        min = prices[0]
        max_profit = 0
        profit = 0
        for price in prices:
            if price < min:
                min = price
            else:
                profit = price - min
                if profit > max_profit:
                    max_profit = profit
                
                
        return max_profit
