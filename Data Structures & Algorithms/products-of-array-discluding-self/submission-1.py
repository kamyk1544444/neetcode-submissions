class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)

        left = [nums[0]]*n
        right=[nums[n-1]]*n
        res = [0]*n

        for i in range(1,n):
            left[i] = nums[i]*left[i-1]
        
        for j in range(n-2,0,-1):
            right[j] = nums[j]*right[j+1]


        for x in range(0,n,1):

            if x==0:
                res[x]=right[x+1]
            elif x==n-1:
                res[x]=left[x-1]
            else:
                res[x] = left[x-1]*right[x+1]

        return res