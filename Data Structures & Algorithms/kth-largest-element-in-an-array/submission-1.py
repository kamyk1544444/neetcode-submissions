class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)

        heapq.heapify(nums)

        x =  n-k

        while x>0:
            heapq.heappop(nums)
            x -=1

        return nums[0]