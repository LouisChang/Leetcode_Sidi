class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        :Newton's Method, use x_{n+1} = 1/2 * (x_n + a/x_n)
        """
        r = x
        while r*r > x:
            r = (r + x/r)/2
        
        return r
