class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        wynik = []

        def dfs(index: int, sub: List[int]):

            if len(sub) == len(nums):
                wynik.append(sub.copy())
                return
            if len(sub) >= len(nums):
                return
            
            for i in range(index,len(nums)):
                sub.append(nums[i])
                nums[i],nums[index] = nums[index],nums[i]
                dfs(index+1,sub)
                nums[i],nums[index] = nums[index],nums[i]
                sub.pop()
        dfs(0,[])
        return wynik 
