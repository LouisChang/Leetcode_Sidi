class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        :time complexity too high:
        
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n-1)  + self.climbStairs(n-2)
        """
        if n == 1:
            return 1
        first, second = 1, 1
        for i in range(1, n+1):
            first, second = second, first + second
            
        return first
