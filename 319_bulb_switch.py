import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        #state = [0]*n
        #count = 0
        """
        : brute force
        # edge case
        if n == 0:
            return 0
        
        for i in range(1,n+1):
            for j in range(1,n/i+1):
                state[j*i-1] = int(not state[j*i-1])
            count += state[i-1]
        
                
        return count
        """
        """
        :find how many square number in the range
        """
        return int(math.sqrt(n))
