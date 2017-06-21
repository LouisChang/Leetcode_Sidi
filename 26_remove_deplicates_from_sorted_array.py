class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        if length < 2:
            return length
        
        count = 0
        for num in range(1, len(nums)):
            if nums[num-1] != nums[num]:
                count += 1
                nums[count] = nums[num]
        
        return count + 1
