class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        new_nums = [nums[i] for i in range(len(nums)) if i%2==0]
        return reduce(lambda x,y:x+y,new_nums)
