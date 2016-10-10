class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_point = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[zero_point],nums[curr] = nums[curr],nums[zero_point]
                zero_point += 1
