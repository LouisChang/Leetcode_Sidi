import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        if n <= 2:
            return 0
        # set the array to be boolean numbers starting from 2,a[0] = 0
        a = [True]*(n)
        # set multiple of i to be False
        # set even number
        for j in range(3,n):
            if j%2 == 0:
                a[j] = False
        for i in range(3,int(math.sqrt(n)+1),2):
            if a[i]:
                #count += 1
                #print(i)
                
                for j in range(2,int(n/i)+1):
                    if j*i == n:
                        continue
                    a[j*i] = False 
                    
        for i in range(3,n,2):
            if a[i]:
                count += 1
        return count
