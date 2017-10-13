# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
# Real world problem, if there is no room available, open a new room; if there is, occupy it.
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        # start and end pointer
        s = e = 0
        # number of rooms and available rooms
        numberOfRooms = availRooms = 0
        while s < len(start):
            if start[s] < end[e]:
                if availRooms == 0:
                    numberOfRooms += 1
                else:
                    availRooms -= 1
                s += 1
            else:
                availRooms += 1
                e += 1
        return numberOfRooms
