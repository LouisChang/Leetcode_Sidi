class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store all the chars in dict
        char_dic = {}
        for c in s:
            if c not in char_dic:
                char_dic[c] = 1
            else:
                char_dic[c] += 1
        
        for i in range(len(s)):
            if char_dic[s[i]] == 1:
                return i
        
        # return -1 if not exist
        return -1
