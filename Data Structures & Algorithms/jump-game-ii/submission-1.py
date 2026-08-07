class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n<=1:
            return 0

        helper = [1000]*n

        helper[0] = 0

        for i in range(n):
            
            for j in range(0,nums[i]+1):

                if i+j < n:
                    helper[j+i] = min(helper[i]+1,helper[j+i])

            
        return helper[n-1]