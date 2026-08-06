class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []
        intervals.sort()
        for i in range(n):

            if i+1 < n and intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0]= min(intervals[i+1][0],intervals[i][0])
                intervals[i+1][1]= max(intervals[i+1][1],intervals[i][1])
            else:
                res.append([intervals[i][0],intervals[i][1]])

        return res