class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        wynik = []

        def dfs(index: int):

            if index == len(nums): 
                wynik.append(nums[:])
                return

            for i in range(index,len(nums)):
                
                nums[i],nums[index] = nums[index],nums[i]
                dfs(index+1,)
                nums[i],nums[index] = nums[index],nums[i]
                
        dfs(0)
        return wynik 
