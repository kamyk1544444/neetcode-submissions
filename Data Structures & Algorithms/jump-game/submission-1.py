class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        n = len(nums)

        dp = [-1]* (n+1)

        dp[0] = 1
        
        for i in range(n):
            if dp[i] == -1:
                continue

            for j in range(1,nums[i]+1):

                print(i,j,nums[i],nums[i]+j)

                if i+j >= n-1:
                    return True
                
                dp[i+j] = 1
        
        return False

                