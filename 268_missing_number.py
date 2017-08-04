class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        
        return n*(n+1)/2 - sum
