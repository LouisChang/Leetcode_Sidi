class Solution(object):
    '''
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dictionary method
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                
        for digit in dic:
            if dic[digit] == 1:
                return digit
        '''
    # bit manipulations
    def singleNumber(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for digit in nums:
            result ^=digit
        
        return result
