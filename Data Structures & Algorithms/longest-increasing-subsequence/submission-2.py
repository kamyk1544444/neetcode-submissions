class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1]*n

        res = 1

        for i in range(0,n-1):
            for j in range(i+1,n):

                if nums[i] < nums[j]:

                    dp[j] = max(dp[j],dp[i]+1)

                res = max(dp[j],res)

        return res