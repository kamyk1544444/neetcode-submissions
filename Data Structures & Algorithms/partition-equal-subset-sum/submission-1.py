class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        suma = 0

        for i in nums:
            suma += i
        
        if suma % 2 != 0:
            return False
        target = suma / 2

        def dfs(index , value) -> bool:


            if value == target:
                return True
            if value > target:
                return False
            if index >= n:
                return False
                
            if dfs(index+1,value+nums[index]):
                return True

            if dfs(index+1,value):
                return True

            return False




        return dfs(0,0)