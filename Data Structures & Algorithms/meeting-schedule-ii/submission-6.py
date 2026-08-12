"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        

        n= len(intervals)

        if n <=1:
            return n
        intervals.sort(key=lambda x:x.start)
        pack = [intervals[0].end]

        for inter in intervals[1:]:

            if pack[0] <= inter.start:
                heapq.heappop(pack)

            heapq.heappush(pack,inter.end)

        return len(pack)