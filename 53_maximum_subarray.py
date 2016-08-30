class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        global_max = 0
        local_max = nums[0]
        sum = 0
        curr = -1
        # check the first positive number and its index, if no positive number, return the first element
        for i in range(len(nums)):
            if nums[i] > local_max:
                local_max = nums[i]
                
        if local_max < 0:
            return local_max
        
        for i in range(len(nums)):
            sum += nums[i]
            if sum > global_max:
                #update global max
                global_max = sum
            if sum <= 0:
                #find next positive number
                sum = 0
        
        return global_max
