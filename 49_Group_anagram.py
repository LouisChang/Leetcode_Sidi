class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            sorted_element = str(sorted(i))
            if sorted_element not in dic:
                dic[sorted_element] = []
                dic[sorted_element].append(i)
            else:
                dic[sorted_element].append(i)
        b = []      
        for i in dic:
            b.append(dic[i])
        
        return b
