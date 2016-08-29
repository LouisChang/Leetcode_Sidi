class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        start = 0
        leng = 0
        i = 0
        if k == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                if leng == k:
                    del dic[nums[start]]
                    start += 1
                    dic[nums[i]] = i
                else:
                    leng += 1
                    dic[nums[i]] = i
                    
        return False
