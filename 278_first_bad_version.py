# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #binary search
        start = 0
        end = n
        mid = (start + end)/2
        while start != end:
            if isBadVersion(mid):
                end = mid
                mid = (start + end)/2
            else:
                start = mid + 1
                mid = (start + end)/2
        
        return start
