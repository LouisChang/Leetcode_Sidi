class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = 1
        else:
            sign = 0
        pos = str(abs(x))
        reverse = pos[::-1]
        reverse = int(reverse)
        if reverse > 2**31 - 1:
            return 0
            
        if sign == 1:
            return 0-reverse
        else:
            return reverse
