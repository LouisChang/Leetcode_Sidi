class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # reflect its point to its coresponding point and compare afterwards
        points = sorted(set(map(lambda x:tuple(x),points)))
        return points == sorted((points[0][0] + points[-1][0] -x, y) for x,y in points)
