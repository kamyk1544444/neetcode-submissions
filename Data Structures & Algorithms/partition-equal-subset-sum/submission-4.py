class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        suma = sum(nums)
        
        if suma % 2 != 0:
            return False

        target = suma / 2

        dp = set()
        dp.add(0)

        for i in range(0,n):
            temp = set()
            for d in dp:
                
                if nums[i]+d == target:
                    return True
                temp.add(d+nums[i])

            dp.update(temp)
            dp.add(nums[i])  

        return False  
