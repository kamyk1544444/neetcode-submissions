class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)

        left = 1
        right=nums[n-1]
        res = [1]*n
        
        for i in range(0,n):
            res[i] = left
            left = nums[i]*left
        
        for j in range(n-2,-1,-1):
            res[j] = right*res[j]
            right = nums[j]*right
            
        return res