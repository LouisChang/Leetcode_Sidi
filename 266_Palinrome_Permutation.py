class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for ele in s:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        count = 1
        for key,item in dic.items():
            if item % 2 ==1:
                count -= 1
            
            if item %2 == 1 and count < 0:
                return False
                
        return True
