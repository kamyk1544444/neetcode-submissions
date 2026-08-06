class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        res = []
        i = 0

        for x,y in intervals:
            if y >= newInterval[0]:
                break
            res.append([x,y])
            i +=1

        for j in range(i,n):

            if intervals[j][0] <= newInterval[1]:
                newInterval[0] = min(intervals[j][0],newInterval[0])
                newInterval[1] = max(intervals[j][1],newInterval[1])
                i +=1
            else:
                break
        res.append([newInterval[0],newInterval[1]])

        for j in range(i,n):
            res.append([intervals[j][0],intervals[j][1]])

        return res
