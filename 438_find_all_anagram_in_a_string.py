class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """
        from collections import Counter
        res = []
        pcount = Counter(p)
        if len(s) >= len(p):
            for i in range(len(s)-len(p)+1):
                scount = Counter(s[i:i+len(p)])
                c = scount - pcount
                if len(c) == 0:
                    res.append(i)
        else:
            return []
                    
        return res
        """
        """
        :moving window, keep a window, delete previous one, add new one
        """
        res = []
        pdic = [0 for i in range(26)]
        for letter in p:
            pdic[ord(letter)-ord('a')] += 1
        rdic = [0 for i in range(26)]
        if len(s) >= len(p):
            for letter in s[0:len(p)]:
                rdic[ord(letter) - ord('a')] += 1
            if rdic == pdic:
                res.append(0)
            for i in range(1,len(s)-len(p)+1):
                rdic[ord(s[i-1])-ord('a')] -= 1
                rdic[ord(s[i+len(p)-1]) - ord('a')] +=1
                if rdic == pdic:
                    res.append(i)
        else:
            return []
        return res


