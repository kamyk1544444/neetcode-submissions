class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        minHeap = []

        for i in range(n):
            val = pow(points[i][0],2) + pow(points[i][1],2)
            heapq.heappush(minHeap,(math.sqrt(val),i))

        
        
        res = []
        while k>0 and minHeap:

            a,b = heapq.heappop(minHeap)
            res.append([points[b][0],points[b][1]])
            k -=1

        return res