class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = 0
        flag = 0
        local_max = 0
        for num in nums:
            if num == 1 and flag == 0:
                flag = 1
            
            if num == 1 and flag == 1:
                local_max += 1
                if local_max > global_max:
                    global_max = local_max
            
            if num == 0:
                local_max = 0
                flag = 0
        return global_max
