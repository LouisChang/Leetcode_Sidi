class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        : Method 1: check the change point method
        
        # flag = -1 means decreasing, flag = 1 means increasing
        total_profit = 0
        # check edge case
        if prices == [] or len(prices)==1:
            return 0
        start = -1
        # find start purchase point
        for i in range(len(prices)-1):
            if prices[i+1] <= prices[i]:
                continue
            else:
                buy = prices[i]
                start = i
                flag = 1
                break
        if start == -1:
            return 0
        for i in range(start+1,len(prices)):
            #price is increasing, if prev is decreasing, buy
            if prices[i] >= prices[i-1]:
                if flag == 1:
                    continue
                else:
                    buy = prices[i-1]
                    flag = 1
            # price is decreasing, if prev is increasing, sell
            else:
                if flag == -1:
                    continue
                else:
                    sell = prices[i-1]
                    flag = -1
                    profit = sell - buy
                    total_profit += profit
                    
        #last element
        if flag == 1:
            total_profit += prices[len(prices)-1]-buy
        
        return total_profit
        """
        """
        :Method 2: slide windows
        """
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                
        return max_profit
