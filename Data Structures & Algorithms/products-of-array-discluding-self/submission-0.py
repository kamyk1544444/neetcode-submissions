class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = 1
        right = 1
        
        n = len(nums)

        res = [0]*n

        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        for j in range(n-1,-1,-1):
            res[j] = res[j]*right
            right *= nums[j]
        
        

        return res



            