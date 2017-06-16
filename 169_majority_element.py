class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        max = 0
        global_key = 0
        for key,value in dic.items():
            if value > max:
                global_key = key
                max = value
                
        return global_key
