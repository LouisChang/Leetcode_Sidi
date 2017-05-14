class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start  = 0
        end = 0
        #sort first
        new = sorted(nums)
        i = 0
        j = len(nums)-1
        while i < len(nums)-1:
            if nums[i] != new[i]:
                start = i
                break
            i +=1
            
        
        while j > 0:
            if nums[j] != new[j]:
                end = j + 1
                break
            j -= 1
        
        return end - start
