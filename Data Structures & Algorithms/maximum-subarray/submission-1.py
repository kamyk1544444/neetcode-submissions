class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        maxim = nums[0]
    

        res = nums[0]

        for i in range(1,len(nums)):

            if maxim <= 0:
                maxim = 0
            maxim += nums[i]
            res = max(maxim,res)

        return res