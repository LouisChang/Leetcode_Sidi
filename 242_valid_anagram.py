"""
class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
 """

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = Counter(s)
        b = Counter(t)
        c = a - b
        d = b - a
        return len(list(c)) == 0 and len(list(d)) == 0
    
    """
    return sorted(s) == sorted(t)
    """
