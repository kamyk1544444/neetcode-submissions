class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        msum,psum = nums[0],nums[0]
        res = nums[0]

        for i in range(1,len(nums)):

            if nums[i]<0:
                psum,msum = msum,psum
            
            psum = max(nums[i],psum*nums[i])
            msum = min(nums[i],msum*nums[i])

            res = max(res,psum)


        return res
            
                
                    
