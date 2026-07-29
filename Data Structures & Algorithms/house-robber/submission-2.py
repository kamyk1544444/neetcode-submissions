class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n<=1:
            return nums[n-1]

        cost = [0] *n

        cost[0] = nums[0]
        cost[1] = max(nums[0],nums[1])

        for i in range(2,n,1):
            cost[i] = max(cost[i-1],cost[i-2]+nums[i])
        
        return max(cost[n-1],cost[n-2])

         