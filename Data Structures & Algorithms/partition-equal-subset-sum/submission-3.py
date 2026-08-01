class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        suma = sum(nums)
        
        if suma % 2 != 0:
            return False
        target = suma / 2

        memo = {}

        def dfs(index , value) -> bool:

            if (index,value) in memo:
                return memo[(index,value)]

            if value == target:
                return True
            if value > target or index >= n:
                return False

            res = dfs(index+1,value+nums[index]) or dfs(index+1,value)
            

            memo[(index,value)] = res

            return res

        return dfs(0,0)