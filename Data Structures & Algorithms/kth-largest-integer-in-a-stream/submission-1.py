class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.minHeap,self.k = nums,k

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap,val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]