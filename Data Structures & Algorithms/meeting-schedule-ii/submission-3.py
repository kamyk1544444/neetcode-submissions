"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        res = []
        heapq.heappush(res,intervals[0].end)
        

        for inter in intervals[1:]:

            if res[0] <= inter.start:
                heapq.heappop(res)
            heapq.heappush(res,inter.end)

        return len(res)


        