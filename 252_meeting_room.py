# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # sort time schedule
        sorted_interval = sorted(intervals, key =lambda intervals: intervals.start)
        for i in range(len(intervals)-1):
            if sorted_interval[i].end > sorted_interval[i+1].start:
                return False
                
        return True
