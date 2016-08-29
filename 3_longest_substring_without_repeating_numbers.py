class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        local_length = 0
        dic = {}
        start = 0
        end = 0
        last =0
        for i in range(len(s)):
            if s[i] not in dic:
                end = i
                dic[s[i]] = i
                local_length += 1
                if local_length > max_length:
                    max_length = local_length
            else:
                start = dic[s[i]]+1
                end = i
                local_length = i - dic[s[i]]
                for j in range(last,start-1):
                    del dic[s[j]]
                last = start
                dic[s[i]] = i
                
        
        return max_length
