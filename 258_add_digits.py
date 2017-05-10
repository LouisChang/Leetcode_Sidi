class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #solution 1
        """
        sum = 0
        while num != 0:
            sum += num % 10
            num /= 10
            if sum/10 !=0 and num  == 0:
                num = sum
                sum = 0
        return sum
        """
        # O(1) time
        """
        : Digital root
        """
        return 1 + (num-1)%9
