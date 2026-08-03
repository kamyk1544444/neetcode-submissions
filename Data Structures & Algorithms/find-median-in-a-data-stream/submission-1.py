class MedianFinder:

    def __init__(self):
        self.large,self.small = [],[]

    def addNum(self, num: int) -> None:
        if self.large and self.large[0] < num:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1*num)
        
        if len(self.small) >  len(self.large):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)  
        if len(self.small)+1 < len(self.large):
            val = -1*heapq.heappop(self.large)
            heapq.heappush(self.small,val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (self.small[0]*-1)
        elif len(self.small) < len(self.large):
            return self.large[0]
        return (self.large[0]+self.small[0]*-1)/2.0
        