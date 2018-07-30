class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # sliding the window and calculate all possiblities after that number
        min_len = len(nums) + 1
        start, end = 0, len(nums)
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            while total_sum >= s:
                min_len = min(min_len, i - start + 1)
                total_sum -= nums[start]
                start += 1
        
        return min_len if min_len != len(nums) + 1 else 0
                
